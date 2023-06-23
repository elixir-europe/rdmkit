import sys
import argparse
import os
import re
from ruamel.yaml import YAML
import re
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import frontmatter

class NullRepresenter:
    def __init__(self):
        self.count = 0

    def __call__(self, repr, data):
         ret_val = repr.represent_scalar(u'tag:yaml.org,2002:null', u'')
         self.count += 1
         return ret_val
         

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

yaml_path = "_data/tool_and_resource_list.yml"
rootdir = 'pages/'
allowed_registries = ['biotools', 'fairsharing', 'tess', 'fairsharing-coll']
my_represent_none = NullRepresenter()


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

args = process_args()
main_list = []

if args.reg:
    fairsharing_token = get_fairsharing_token(args.username, args.password)
with open(yaml_path, 'r') as read_obj:
    yaml=YAML(typ='safe')
    yaml.default_flow_style = False
    yaml.representer.add_representer(type(None), my_represent_none)
    all_tools = yaml.load(read_obj)

    # Looping over tools
    for i, tool in enumerate(all_tools):
        if tool['id'] != re.sub('[^0-9a-zA-Z]+', ' ', re.sub("[\(\[].*?[\)\]]", "", tool['id'])).strip().replace(" ", "-").lower():
            sys.exit(f"{tool['name']} has an incorrect ID")
        tool_name = tool['name']
        # Only include keys if there are values:
        if 'related_pages' in tool and tool['related_pages']:
            print( f'ERROR: The tool "{tool_name}" contains `related_pages` as metadata field, which is not supported.\n')
            sys.exit()
        if 'registry' in tool and tool['registry']:
            for registry, identifier in tool['registry'].items():
                if registry not in allowed_registries:
                    print(
                        f'ERROR: The table contains the registry "{registry}" in row which is not allowed.\n' + f"Allowed registries are {', '.join(allowed_registries)}.\n")
                    sys.exit(
                        f'The table contains the registry "{registry}" in row which is not allowed.\n' + f"Allowed registries are {', '.join(allowed_registries)}.\n")

# --------- Pulling from FAIRsharing, TeSS and Bio.tools ---------
            if args.reg:
                # TeSS Lookup
                check_tess = tess_available(tool_name)
                if check_tess:
                    tool['registry']["tess"] = check_tess
                else: 
                    if "tess" in tool['registry'].keys():
                        del tool['registry']["tess"]
                # Bio.tools Lookup
                if "biotools" not in tool['registry'].keys() or not tool['registry']["biotools"] :
                    check_biotools = biotools_available(tool_name)
                    if check_biotools:
                        tool['registry']["biotools"] = check_biotools
                if "biotools" in tool['registry'].keys() and not tool['registry']["biotools"]:
                    del tool['registry']["biotools"]

                # FAIRsharing Lookup
                if "fairsharing" not in tool['registry'].keys() or not tool['registry']["fairsharing"]:
                    if len(tool_name) > 4:
                        check_fairsharing = fairsharing_available(
                            tool_name, fairsharing_token)
                        if check_fairsharing:
                            tool['registry']["fairsharing"] = check_fairsharing
                if "fairsharing" in tool['registry'].keys() and not tool['registry']["fairsharing"]:
                    del tool['registry']["fairsharing"]
        main_list.append(tool)
        print(f"{i}. {tool['name']} is parsed.")

with open(yaml_path, 'w') as yaml_file:
    yaml.dump(main_list, yaml_file)

print("----> YAML is dumped successfully")
