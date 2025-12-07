import os
import re
import requests
import yaml
import json
from datetime import date
import argparse
import frontmatter

# --------- Config ---------
PAGES_DIR = "pages/your_domain"
RDMKIT_BASE_URL = "https://rdmkit.elixir-europe.org"
RDMKIT_GITHUB_BASE = "https://github.com/elixir-europe/rdmkit/blob/master"
# FAIRSHARING_API = "https://api.fairsharing.org/"      # FAIRsharing PRODUCTION API
# FAIRSHARING_URL = "https://fairsharing.org/"          # FAIRsharing PRODUCTION
FAIRSHARING_API = "https://dev-api.fairsharing.org/"    # FAIRsharing DEV API
FAIRSHARING_URL = "https://preview.fairsharing.org/"    # FAIRsharing DEV


# ----------------- Helpers -----------------

def process_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="Create/Update FAIRsharing collections",
        description=(
            "This script loops over the domain pages and creates or updates a FAIRsharing "
            "collection based on the FAIRsharing identifiers in the tools and "
            "resources mentioned in the page."
        ),
    )
    parser.add_argument("--username", help="Specify the FAIRsharing username")
    parser.add_argument("--password", help="Specify the FAIRsharing password")
    return parser.parse_args()


def return_fs_doi(m):
    """Return FAIRsharing DOI from a tool/resource metadata dict."""
    doi = None
    if "registry" in m:
        if "fairsharing" in m["registry"]:
            if m["registry"]["fairsharing"] != "NA":
                doi = m["registry"]["fairsharing"]
    return doi


def is_record_collected(linked_records, id_to_check):
    """Check whether a record is already 'collects' in linked_records list."""
    for i in linked_records:
        if i.get("linked_record_id") == id_to_check and i.get("relation") == "collects":
            return True
    return False


def find_tools_in_markdown(text):
    """
    Looks for pattern:
      {% tool "TOOL_ID" ... %}
    and returns the TOOL_ID tokens.
    """
    tools = []
    prev_word = ""
    to_save = False
    for word in text.split():
        if to_save:
            t = word.replace('"', "").replace("'", "")
            if t not in tools:
                tools.append(t)
            to_save = False
        if word == "tool" and "{%" in prev_word:
            to_save = True
        prev_word = word
    return tools


def extract_fairsharing_id_from_url(url: str):
    """
    Extract numeric FAIRsharing record id from URL like:
      https://fairsharing.org/3533
    Returns int or None.
    """
    if not url:
        return None
    parts = url.strip().rstrip("/").split("/")
    last = parts[-1]
    if last.isdigit():
        return int(last)
    return None


def authenticate(username, password):
    """Authenticate against FAIRsharing and return headers, user_id, user_name."""
    payload = json.dumps({"user": {"login": username, "password": password}})
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(FAIRSHARING_API + "users/sign_in", headers=headers, data=payload)
    response.raise_for_status()
    data = response.json()
    jwt = data["jwt"]
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt}",
    }
    return headers, data["id"], data["username"]


def get_collects_label_id(headers):
    """Return the id of the 'collects' record_association_label."""
    response = requests.get(FAIRSHARING_API + "record_association_labels", headers=headers)
    if not response.ok:
        print("Error when retrieving record_association_labels")
        print(response.text)
        return None

    record_association_labels = response.json()
    for i in record_association_labels:
        if i["name"] == "collects":
            return i["id"]

    print("Error: the collection relation ID 'collects' is not found")
    return None


def parse_frontmatter_boundaries(contents):
    """
    Detect frontmatter and fairsharing block boundaries using the DSW logic.
    Returns (frontmatter_start, frontmatter_end, fs_start, fs_end).
    """
    frontmatter_start = False
    frontmatter_end = 0
    fs_start = 0
    fs_end = 0

    for index, line in enumerate(contents):
        if re.match(r"^---", line):
            if isinstance(frontmatter_start, bool):
                frontmatter_start = index
            else:
                frontmatter_end = index
                if fs_start and not fs_end:
                    fs_end = index
        elif line.startswith("fairsharing:") and isinstance(frontmatter_start, int):
            fs_start = index
        elif (
            re.match(r"^[a-zA-Z]", line)
            and isinstance(frontmatter_start, int)
            and fs_start
            and not fs_end
        ):
            fs_end = index
        if frontmatter_end:
            break

    return frontmatter_start, frontmatter_end, fs_start, fs_end


def build_collections_to_check():
    """
    Walk pages, read metadata via frontmatter, and raw contents via DSW method.
    Returns (collections_to_check, all_tools).
    """
    collections_to_check = {}
    all_tools = []

    for subdir, dirs, files in os.walk(PAGES_DIR):
        for file_name in files:
            if os.path.splitext(file_name)[1] != ".md":
                continue
            if file_name.startswith("TEMPLATE_"):
                # Skip templates
                continue

            filename_stripped = os.path.splitext(file_name)[0]
            path = os.path.join(subdir, file_name)
            print(f"Reading out {filename_stripped}")

            # --- Read raw contents for later write-back ---
            with open(path, "r", encoding="utf8") as f:
                contents = f.readlines()

            frontmatter_start, frontmatter_end, fs_start, fs_end = parse_frontmatter_boundaries(
                contents
            )

            if not isinstance(frontmatter_start, int) or frontmatter_end == 0:
                print(f"\tNo valid frontmatter found in {path}, skipping.")
                continue

            # --- Use python-frontmatter to read metadata and content ---
            post = frontmatter.load(path)
            metadata = post.metadata or {}

            title = metadata.get("title")
            if not title:
                print(f"\tPage {path} has no frontmatter 'title' — skipping.")
                continue

            existing_fs = metadata.get("fairsharing")
            existing_record_id = None
            has_fs_meta = False

            if isinstance(existing_fs, list) and existing_fs:
                has_fs_meta = True
                for entry in existing_fs:
                    if isinstance(entry, dict) and "url" in entry:
                        existing_record_id = extract_fairsharing_id_from_url(entry["url"])
                        if existing_record_id is not None:
                            break

            # Determine tools from the body using post.content
            tools_in_page = find_tools_in_markdown(post.content)

            # Collect tools globally
            for t in tools_in_page:
                if t not in all_tools:
                    all_tools.append(t)

            # Build GitHub ref URL using relative path for robustness
            rel_path = os.path.relpath(path, ".").replace(os.sep, "/")
            slug = filename_stripped

            collections_to_check[path] = {
                "record": None,
                "record_id": existing_record_id,
                "has_fs_meta": has_fs_meta,
                "tools": tools_in_page,
                "domain": title,
                "new_name": f"RDMkit {title} Domain",
                "new_homepage": f"{RDMKIT_BASE_URL}/{slug}",
                "new_ref_url": f"{RDMKIT_GITHUB_BASE}/{rel_path}",
                "contents": contents,
                "frontmatter_start": frontmatter_start,
                "frontmatter_end": frontmatter_end,
                "fs_start": fs_start,
                "fs_end": fs_end,
            }

    return collections_to_check, all_tools


def load_tool_metadata():
    """Load local RDMkit tool list from YAML."""
    with open("_data/tool_and_resource_list.yml", "r", encoding="utf8") as f:
        return yaml.safe_load(f)


def build_matched_items(all_tools, data_list, headers):
    """
    Build mapping from RDMkit tool id -> FAIRsharing record id (if any).
    Uses FAIRsharing content_negotiation endpoint to resolve DOIs.
    """
    doi_to_id = {}
    matched_items = {}

    for t in all_tools:
        for item in data_list:
            if item.get("id") == t:
                matched_items[t] = {"rdm": item, "id_fs": None}
                break

    for m in matched_items:
        fs_doi = return_fs_doi(matched_items[m]["rdm"])
        if fs_doi is not None:
            if fs_doi not in doi_to_id:
                response = requests.get(
                    "https://api.fairsharing.org/content_negotiation/json/FAIRsharing."
                    + fs_doi,
                    headers=headers,
                )
                if response.ok:
                    d = response.json()
                    doi_to_id[fs_doi] = int(d["id"])
                else:
                    print("Error getting FAIRsharing record for DOI", fs_doi)
                    print(response.text)
                    continue
            matched_items[m]["id_fs"] = doi_to_id[fs_doi]

    return matched_items


def get_subject_and_taxonomy_ids(headers):
    """Return (subject_ids_to_add, taxon_ids_to_add)."""
    subject_ids_to_add = []
    response = requests.post(
        FAIRSHARING_API + "search/subjects?q=life science", headers=headers
    )
    if response.ok:
        subjects_data = response.json().get("data", [])
        for d in subjects_data:
            if d["label"].lower() == "life science":
                subject_ids_to_add.append(d["id"])
                break
    else:
        print("Error retrieving subjects")
        print(response.text)

    taxon_ids_to_add = []
    response = requests.post(
        FAIRSHARING_API + "search/taxonomies?q=not applicable", headers=headers
    )
    if response.ok:
        tax_data = response.json()
        for d in tax_data:
            if d["label"].lower() == "not applicable":
                taxon_ids_to_add.append(d["id"])
                break
    else:
        print("Error retrieving taxonomies")
        print(response.text)

    return subject_ids_to_add, taxon_ids_to_add


def create_new_collection(colinfo, headers, user_name, user_id,
                          subject_ids_to_add, taxon_ids_to_add):
    """Create a new FAIRsharing collection and return (record, record_id, record_name, fairsharing_url)."""
    new_record = {}
    new_record["fairsharing_record"] = {}
    new_record["fairsharing_record"]["is_data_set"] = False
    new_record["fairsharing_record"]["dups_suspected"] = False
    new_record["fairsharing_record"]["record_type_id"] = 15
    new_record["fairsharing_record"]["country_ids"] = []
    new_record["fairsharing_record"]["metadata"] = {}
    new_record["fairsharing_record"]["metadata"]["name"] = colinfo["new_name"]
    new_record["fairsharing_record"]["metadata"]["homepage"] = colinfo["new_homepage"]
    new_record["fairsharing_record"]["metadata"]["reference_url"] = colinfo["new_ref_url"]
    new_record["fairsharing_record"]["metadata"]["year_creation"] = date.today().year
    new_record["fairsharing_record"]["metadata"]["description"] = (
        "This collection has been created via a collaboration between FAIRsharing and "
        "RDMkit to provide a live representation of those standards and databases "
        f"described within the {colinfo['domain']} domain pages of RDMKit."
    )
    new_record["fairsharing_record"]["metadata"]["status"] = "ready"
    new_record["fairsharing_record"]["maintainers"] = []
    maint = {"username": user_name, "id": user_id}
    new_record["fairsharing_record"]["maintainers"].append(maint)
    contact = {
        "contact_name": "RDMKit Editors",
        "contact_email": "rdm-editors@elixir-europe.org",
    }
    new_record["fairsharing_record"]["metadata"]["contacts"] = [contact]
    new_record["fairsharing_record"]["subject_ids"] = subject_ids_to_add
    new_record["fairsharing_record"]["taxonomy_ids"] = taxon_ids_to_add

    json_object = json.dumps(new_record, indent=4)
    response = requests.post(
        FAIRSHARING_API + "fairsharing_records", headers=headers, data=json_object
    )
    if not response.ok:
        print("Error creating new FAIRsharing record")
        print(response.text)
        return None, None, None, None

    data = response.json()["data"]
    record = data["attributes"]
    record["linked_records"] = record.get("linked_records", [])
    record_id = int(data["id"])
    record_name = record["metadata"]["name"]
    fairsharing_url = f"{FAIRSHARING_URL}{record_id}"

    # Create organisation links
    organisation_link = {"organisation_link": {}}
    organisation_link["organisation_link"]["fairsharing_record_id"] = record_id
    organisation_link["organisation_link"]["organisation_id"] = 841
    organisation_link["organisation_link"]["relation"] = "collaborates_on"
    json_object = json.dumps(organisation_link, indent=4)
    requests.post(
        FAIRSHARING_API + "organisation_links", headers=headers, data=json_object
    )

    organisation_link["organisation_link"]["organisation_id"] = 4764
    organisation_link["organisation_link"]["relation"] = "maintains"
    organisation_link["organisation_link"]["is_lead"] = True
    json_object = json.dumps(organisation_link, indent=4)
    requests.post(
        FAIRSHARING_API + "organisation_links", headers=headers, data=json_object
    )

    return record, record_id, record_name, fairsharing_url


def fetch_existing_collection(record_id, headers):
    """Fetch an existing FAIRsharing collection by id."""
    response = requests.get(
        FAIRSHARING_API + "fairsharing_records/" + str(record_id),
        headers=headers,
    )
    if not response.ok:
        print("Error retrieving existing FAIRsharing record")
        print(response.text)
        return None, None, None

    rec_data = response.json()["data"]["attributes"]
    rec_data["linked_records"] = rec_data.get("linked_records", [])
    record_name = rec_data["metadata"]["name"]
    fairsharing_url = f"{FAIRSHARING_URL}{record_id}"
    return rec_data, record_name, fairsharing_url


def sync_record_associations(colinfo, matched_items, collec_lab_id, headers):
    """
    Sync the collection's linked_records with the tools found in the page:
    - Remove associations that are no longer present.
    - Add new ones for tools that appear and have FAIRsharing ids.
    """
    # 1. Compute FAIRsharing ids for tools in this page
    tools_id_to_add = []
    for t in colinfo["tools"]:
        if t in matched_items and matched_items[t]["id_fs"] is not None:
            tools_id_to_add.append(matched_items[t]["id_fs"])

    # 2. Remove relations that are no longer in RDMkit
    for link_rec in list(colinfo["record"]["linked_records"]):
        lr_id = link_rec.get("linked_record_id")
        if lr_id not in tools_id_to_add:
            link_id = link_rec.get("link_id")
            if link_id is None:
                continue
            response = requests.delete(
                FAIRSHARING_API + "record_associations/" + str(link_id),
                headers=headers,
            )
            if response.ok:
                print(
                    f"In the FAIRsharing collection {colinfo['record_id']} the relation "
                    f"with the record {lr_id} is removed."
                )
            else:
                print("Error removing record_association")
                print(response.text)

    # 3. Create missing relations
    num_relations = 0
    for id_rec in tools_id_to_add:
        if not is_record_collected(colinfo["record"]["linked_records"], id_rec):
            record_association = {"record_association": {}}
            record_association["record_association"]["fairsharing_record_id"] = colinfo[
                "record_id"
            ]
            record_association["record_association"]["linked_record_id"] = id_rec
            record_association["record_association"]["record_assoc_label_id"] = collec_lab_id
            json_object = json.dumps(record_association, indent=4)
            response = requests.post(
                FAIRSHARING_API + "record_associations",
                headers=headers,
                data=json_object,
            )
            if response.ok:
                num_relations += 1
            else:
                print("Error creating record_association")
                print(response.text)

    print(
        f"For the record {colinfo['record_id']} {num_relations} records are collected/added"
    )


def update_frontmatter_if_needed(path, colinfo, record_name, fairsharing_url):
    """
    Use the DSW-style logic to inject a fairsharing block if it's not present.
    Does NOT remove or modify existing fairsharing frontmatter.
    """
    contents = colinfo["contents"]
    frontmatter_end = colinfo["frontmatter_end"]
    fs_start = colinfo["fs_start"]
    fs_end = colinfo["fs_end"]

    # If previous fairsharing block does not exist, add it
    if not fs_start and not fs_end and not colinfo["has_fs_meta"]:
        fs_metadata = {
            "fairsharing": [
                {
                    "name": record_name,
                    "url": fairsharing_url,
                }
            ]
        }
        contents.insert(
            frontmatter_end,
            yaml.dump(fs_metadata, default_flow_style=False),
        )
        print(f"\tNew fairsharing block inserted in content")

        print(f"\tDumping content in markdown file {path}")
        with open(path, "w", encoding="utf8") as f:
            contents_str = "".join(contents)
            f.write(contents_str)
        print(f"\tDone")
    else:
        print("\tFairsharing frontmatter already present, not modifying it.")


# ----------------- Main -----------------

def main():
    args = process_args()

    # 1. Authenticate
    headers, user_id, user_name = authenticate(args.username, args.password)

    # 2. 'collects' label id
    collec_lab_id = get_collects_label_id(headers)
    if collec_lab_id is None:
        return

    # 3. Build pages / collections to check
    collections_to_check, all_tools = build_collections_to_check()
    if not collections_to_check:
        print("No pages to process.")
        return

    # 4. Load tool metadata & FAIRsharing ids
    data_list = load_tool_metadata()
    matched_items = build_matched_items(all_tools, data_list, headers)

    # 5. Subjects & taxonomies
    subject_ids_to_add, taxon_ids_to_add = get_subject_and_taxonomy_ids(headers)

    # 6. Process each page
    for path, colinfo in collections_to_check.items():
        print(f"\nPerforming actions for page {path}")

        # Case A: frontmatter has fairsharing metadata but no parseable id -> skip
        if colinfo["record_id"] is None and colinfo["has_fs_meta"]:
            print(
                "\tFrontmatter contains a fairsharing block, but no valid numeric id could be parsed. "
                "Skipping to avoid mismatching collections."
            )
            continue

        # Case B: create new collection
        if colinfo["record_id"] is None:
            record, record_id, record_name, fairsharing_url = create_new_collection(
                colinfo, headers, user_name, user_id, subject_ids_to_add, taxon_ids_to_add
            )
            if record is None:
                continue
            colinfo["record"] = record
            colinfo["record_id"] = record_id
        # Case C: existing collection -> fetch
        else:
            print(f"\tExisting FAIRsharing collection id found: {colinfo['record_id']}")
            record, record_name, fairsharing_url = fetch_existing_collection(
                colinfo["record_id"], headers
            )
            if record is None:
                continue
            colinfo["record"] = record

        # Sync tool relations
        sync_record_associations(colinfo, matched_items, collec_lab_id, headers)

        # Update frontmatter only if fairsharing is missing
        update_frontmatter_if_needed(path, colinfo, record_name, fairsharing_url)

    print("FAIRsharing collections successfully created/updated for domain pages.")


if __name__ == "__main__":
    main()
