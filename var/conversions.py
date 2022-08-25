import sys
import argparse
import os
import re
from csv import reader
import yaml
import re
import unicodedata
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import frontmatter


def process_args():
    '''parse command-line arguments
    '''

    parser = argparse.ArgumentParser(prog='Conversions',
                                     description='This script will convert the tool and resources table to a yaml file while injecting bio.tools and FAIRsharing IDs where needed.',)
    parser.add_argument('--username',
                        help='Specify the FAIRsharing username')

    parser.add_argument('--password',
                        help='Specify the FAIRsharing password')

    parser.add_argument('--reg',
                        default=False,
                        action="store_true",
                        help='Enable TeSS, bio.tools and FAIRsharing lookup')

    args = parser.parse_args()

    return args


def parse_acronym(query):
    m = re.match(r"(.*)\s\((.*)\)", query)
    if m:
        return {"fullname": m.group(1), "acronym": m.group(2)}


def client(url):
    """API object fetcher"""
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=15)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    r = session.get(url)
    if r.status_code == requests.codes.ok:
        return r.json()


def tess_available(query):
    acronym = parse_acronym(query)
    def fetch_output(query):
        return client(
            f'https://tess.elixir-europe.org/materials.json_api?q="{query}"&page_number=1&page_size=30')
    if len(fetch_output(query)['data']) > 0:
        return query
    if acronym and len(fetch_output(acronym['fullname'])['data']) > 0:
        return acronym['fullname']


def biotools_available(query):
    acronym = parse_acronym(query)
    if acronym and client(f"https://bio.tools/api/tool/{acronym['acronym'].lower()}/?format=json"):
        return acronym['acronym'].lower()
    elif client(f"https://bio.tools/api/tool/{query.lower()}/?format=json"):
        return query.lower()
    elif len(query) > 4:
        json_output = client(
            f"https://bio.tools/api/t/?format=json&q='{query}'")
        if json_output['count'] != 0:
            for tool in json_output['list']:
                if tool['name'].lower() == query.strip().lower():
                    return tool['biotoolsID']
        else:
            json_output = client(
                f"https://bio.tools/api/t/?format=json&q='{query}'")
            if json_output['count'] != 0:
                for tool in json_output['list']:
                    if query.strip().lower() in tool['name'].lower():
                        return tool['biotoolsID']


def get_fairsharing_token(username, password):
    url = "https://api.fairsharing.org/users/sign_in"
    payload = "{\"user\": {\"login\":\"" + username + \
        "\",\"password\":\"" + password + "\"} }"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.json()["success"] != True:
            sys.exit()
        else:
            return response.json()["jwt"]
    except:
        print("Could not login into FAIRsharing")


def fairsharing_available(query, token):
    url = "https://api.fairsharing.org/search/fairsharing_records"

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    payload = {'q': query}
    try:
        response = requests.request(
            "POST", url, headers=headers, params=payload)
        output = response.json()['data']
        if len(output) >= 1:
            for fairsharing_obj in output:
                if query.lower() in fairsharing_obj['attributes']['name'].lower() and fairsharing_obj['attributes']['doi']:
                    return fairsharing_obj['attributes']['url'].split(".")[-1]
    except:
        print(response)
        sys.exit("Could not connect to FAIRsharing")


def remove_prefix(s, prefix):
    return s[s[:len(prefix)].index(prefix) + len(prefix):]

# --------- Variables ---------


table_path = "_data/main_tool_and_resource_list.csv"
output_path = "_data/tool_and_resource_list.yml"
rootdir = 'pages/'
allowed_registries = ['biotools', 'fairsharing', 'tess', 'fairsharing-coll']


# --------- Reading out page_ids from pages ---------

print(f"----> Reading out page_id from each file")
pages_metadata = {}
for subdir, dirs, files in os.walk(rootdir):
    for file_name in files:
        if os.path.splitext(file_name)[1] == '.md':
            print(f"Opening {os.path.splitext(file_name)[0]}")
            with open(os.path.join(subdir, file_name)) as f:
                metadata, content = frontmatter.parse(f.read())
            if 'page_id' in metadata.keys() and 'search_exclude' not in metadata.keys():
                pages_metadata[metadata['page_id']] = {}
                pages_metadata[metadata['page_id']
                               ]['title'] = metadata['title']
                pages_metadata[metadata['page_id']]['type'] = remove_prefix(
                    subdir, 'pages/').replace("_", " ").capitalize()
                pages_metadata[metadata['page_id']]['url'] = os.path.splitext(file_name)[
                    0]
                if 'description' in metadata:
                    pages_metadata[metadata['page_id']
                                   ]['description'] = metadata['description']

print(f"----> Allowed related_pages: {', '.join(pages_metadata.keys())}.")

# --------- Converting the table ---------

print(f"----> Converting table {table_path} to {output_path} started.")
args = process_args()
main_list = []
if args.reg:
    fairsharing_token = get_fairsharing_token(args.username, args.password)
with open(table_path, 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Looping over rows and adding its contents to the main dict
        for row_index, row in enumerate(csv_reader):
            tool = {}
            tool_name = row[0]
            for col_index, cell in enumerate(row):
                # Only include keys if there are values:
                if header[col_index] == 'related_pages' and cell:
                    output = re.split(', |,', cell)
                    for tag in output:
                        if tag not in pages_metadata.keys():
                            print(
                                f'ERROR: The table contains the tag "{tag}" in row {row_index} which is not allowed.\n-> Check if the tag you are using is declared in the metadata of one of the pages using the "page_id" attribute.')
                            sys.exit(
                                f'The table contains the tag "{tag}" in row {row_index} which is not allowed.\n-> Check if the tag you are using is declared in the metadata of one of the pages using the "page_id" attribute.')
                # Only include keys if there are values:
                elif header[col_index] == 'country' and cell:
                    output = re.split(', |,', cell)
                elif header[col_index] == 'registry':
                    output = {}
                    if cell:  # Only include keys if there are values
                        for registry in re.split(', |,', cell):
                            reg, identifier = re.split(':|: ', registry)
                            if reg in allowed_registries:
                                output[reg] = identifier
                            else:
                                print(
                                    f'ERROR: The table contains the registry "{reg}" in row {row_index} which is not allowed.\n' + f"Allowed registries are {', '.join(allowed_registries)}.\n")
                                sys.exit(
                                    f'The table contains the registry "{reg}" in row {row_index} which is not allowed.\n' + f"Allowed registries are {', '.join(allowed_registries)}.\n")
                    if args.reg:
                        if "tess" not in output:
                            check_tess = tess_available(tool_name)
                            if check_tess:
                                output["tess"] = check_tess
                        elif output["tess"] == "NA":
                            del output["tess"]
                        if "biotools" not in output:
                            check_biotools = biotools_available(tool_name)
                            if check_biotools:
                                output["biotools"] = check_biotools
                        elif output["biotools"] == "NA":
                            del output["biotools"]
                        if "fairsharing" not in output:
                            if len(tool_name) > 4:
                                check_fairsharing = fairsharing_available(
                                    tool_name, fairsharing_token)
                                if check_fairsharing:
                                    output["fairsharing"] = check_fairsharing
                        elif output["fairsharing"] == "NA":
                            del output["fairsharing"]
                else:
                    # Return the normal form for the Unicode string
                    output = unicodedata.normalize("NFKD", cell).strip()
                if output:
                    tool[header[col_index]] = output
            main_list.append(tool)
            print(f"{row_index}. {tool['name']} is parsed.")

with open(output_path, 'w') as yaml_file:
    documents = yaml.dump(main_list, yaml_file)

print("----> YAML is dumped successfully")
