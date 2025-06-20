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
from urllib.parse import urlparse

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

    parser = argparse.ArgumentParser(prog='Tools Validator',
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
    acronym = parse_acronym(query)
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
                elsif acronym['fullname'] in fairsharing_obj['attributes']['name'].lower() and fairsharing_obj['attributes']['doi']:
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

args = process_args()
main_list = []

if args.reg:
    fairsharing_token = get_fairsharing_token(args.username, args.password)
with open(yaml_path, 'r') as read_obj:
    yaml=YAML(typ='safe')
    yaml.default_flow_style = False
    yaml.representer.add_representer(type(None), my_represent_none)
    yaml.width = 1000
    all_tools = yaml.load(read_obj)

    # Looping over tools
    for i, tool in enumerate(all_tools):
        if 'id' not in tool.keys() or tool['id'] != re.sub('[^0-9a-zA-Z]+', ' ', re.sub("[\(\[].*?[\)\]]", "", tool['id'])).strip().replace(" ", "-").lower():
            sys.exit(f"{tool['name']} has an no or incorrect ID. Make sure the ID is kebab-case and only contains alphanumerical characters.")
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
        if 'url' in tool and tool['url']:
            validation = urlparse(tool['url'])
            if not validation.scheme and not validation.netloc:
                print( f'ERROR: The tool "{tool_name}" contains has an invalid url: {tool["url"]}\n')
                sys.exit()


# --------- Pulling from FAIRsharing, TeSS and Bio.tools ---------
            if args.reg:
                registry = {}
                if 'registry' in tool:
                    registry = tool['registry']
                # TeSS Lookup
                check_tess = tess_available(tool_name)
                if check_tess:
                    registry['tess'] = check_tess
                else: 
                    if 'tess' in registry.keys():
                        del registry['tess']
                # Bio.tools Lookup
                if 'biotools' not in registry.keys() or not registry['biotools'] :
                    check_biotools = biotools_available(tool_name)
                    if check_biotools:
                        registry['biotools'] = check_biotools
                if 'biotools' in registry.keys() and not registry['biotools']:
                    del registry['biotools']

                # FAIRsharing Lookup
                if 'fairsharing' not in registry.keys() or not registry['fairsharing']:
                    if len(tool_name) > 4:
                        check_fairsharing = fairsharing_available(
                            tool_name, fairsharing_token)
                        if check_fairsharing:
                            registry['fairsharing'] = check_fairsharing
                if 'fairsharing' in registry.keys() and not registry['fairsharing']:
                    del registry['fairsharing']

                # Add populated registry dict to the main list
                if registry:
                    tool['registry'] = registry
                # Delete empty dict
                if 'registry' in tool and not tool['registry']:
                    del tool['registry']
        main_list.append(tool)
        print(f"{i}. {tool['name']} is parsed.")

with open(yaml_path, 'w') as yaml_file:
    yaml.dump(main_list, yaml_file)

print("----> YAML is dumped successfully")
