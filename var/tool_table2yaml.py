import sys
from csv import reader
import yaml
import re
import unicodedata
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def client(url):
    """API object fetcher"""
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=15)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    r = session.get(url)
    if r.status_code != requests.codes.ok:
        return False
    else:
        return r.json()


def tess_available(query):
    json_output = client(
        f"https://tess.elixir-europe.org/materials?q={query}&page_number=1&page_size=30")
    if len(json_output) > 0:
        return True

def biotools_available(query):
    if client(f"https://bio.tools/api/tool/{query.lower()}/?format=json"):
        return query.lower()
    else:
        json_output = client(
            f"https://bio.tools/api/t/?format=json&q='{query}'")
        if json_output['count'] != 0:
            for tool in json_output['list']:
                if tool['name'].lower() == query.strip().lower():
                    return tool['biotoolsID']
        else:
            json_output = client(
                f"https://bio.tools/api/t/?format=json&q='{query}'")
            if json_output['count'] == 0:
                return False
            else:
                for tool in json_output['list']:
                    if query.strip().lower() in tool['name'].lower():
                        return tool['biotoolsID']
        return False



table_path = "_data/main_tool_and_resource_list.csv"
output_path = "_data/tool_and_resource_list.yml"
main_dict_key = "Tools"
allowed_tags_yaml = "_data/tags.yml"
allowed_registries = ['biotools', 'fairsharing', 'tess']

print(f"----> Converting table {table_path} to {output_path} started.")

with open(allowed_tags_yaml) as file:
    allowed_tags = yaml.load(file, Loader=yaml.FullLoader)

print(f"----> Allowed tags: {', '.join(allowed_tags)}.")
main_dict = {main_dict_key: []}
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
                if header[col_index] == 'tags' and cell:# Only include keys if there are values:
                    output = re.split(', |,', cell)
                    for tag in output:
                        if tag not in allowed_tags:
                            print(f'ERROR: The table contains the tag "{tag}" in row {row_index} which is not allowed.\n-> Check out the tool_tags.yaml file in the _data directory to find out the allowed tags.')
                            sys.exit(
                                f'The table contains the tag "{tag}" in row {row_index} which is not allowed.\n-> Check out the tool_tags.yaml file in the _data directory to find out the allowed tags.')
                elif header[col_index] == 'registry':
                    output = {}
                    if cell:# Only include keys if there are values
                        for registry in re.split(', |,', cell):
                            reg, identifier = re.split(':|: ', registry)
                            if reg in allowed_registries:
                                output[reg] = identifier
                            else:
                                print(f'ERROR: The table contains the registry "{reg}" in row {row_index} which is not allowed.\n' + f"Allowed registries are {', '.join(allowed_registries)}.\n")
                                sys.exit(
                                    f'The table contains the registry "{reg}" in row {row_index} which is not allowed.\n' + f"Allowed registries are {', '.join(allowed_registries)}.\n")
                    if len(sys.argv) > 1 and sys.argv[1] == "--reg":
                        if tess_available(tool_name):
                            if "tess" not in output:
                                output["tess"] = tool_name
                            elif output["tess"] == "NA":
                                del output["tess"]
                        if biotools_available(tool_name):
                            if "biotools" not in output:
                                output["biotools"] = biotools_available(tool_name)
                            elif output["biotools"] == "NA":
                                del output["biotools"]
                else:
                    # Return the normal form for the Unicode string
                    output = unicodedata.normalize("NFKD", cell).strip()
                if output:
                    tool[header[col_index]] = output
            main_dict[main_dict_key].append(tool)
            print(f"{row_index}. {tool['name']} is parsed.")

with open(output_path, 'w') as yaml_file:
    documents = yaml.dump(main_dict, yaml_file)

print("----> YAML is dumped successfully")
