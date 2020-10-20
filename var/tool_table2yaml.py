import sys
from csv import reader
import yaml
import re
import unicodedata

table_path = "_data/main_tool_and_resource_list.csv"
output_path = "_data/tool_and_resource_list.yml"
main_dict_key = "Tools"
allowed_tags_yaml = "_data/tags.yml"
allowed_registries = ['biotools', 'fairsharing']

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
            for col_index, cell in enumerate(row):
                if cell: # Only include keys if there are values
                    if  header[col_index] == 'tags':
                        output = re.split(', |,', cell)
                        for tag in output:
                            if tag not in allowed_tags:
                                sys.exit(f'The table contains the tag "{tag}" in row {row_index} which is not allowed.\n-> Check out the tool_tags.yaml file in the _data directory to find out the allowed tags.')
                    elif header[col_index] == 'registry':
                        output={}
                        for registry in re.split(', |,', cell):
                            reg, identifier = re.split(':', registry)
                            if reg in allowed_registries:
                                output[reg] = identifier
                            else:
                                sys.exit(f'The table contains the registry "{reg}" in row {row_index} which is not allowed.\n')
                    else:
                        output = unicodedata.normalize("NFKD", cell).strip() # Return the normal form for the Unicode string
                    tool[header[col_index]] = output
            main_dict[main_dict_key].append(tool)
            print(f"{row_index}. {tool['name']} is parsed.")

with open(output_path, 'w') as yaml_file:
    documents = yaml.dump(main_dict, yaml_file)

print("----> YAML is dumped successfully")