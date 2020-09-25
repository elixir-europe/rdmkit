import sys
import xlrd
import yaml
import re
import unicodedata

table_path = "_data/tool_and_resource_list.xlsx"
output_path = "_data/tool_and_resource_list.yml"
main_dict_key = "Tools"
allowed_tags_yaml = "_data/tags.yml"
allowed_registries = ['biotools', 'fairsharing']

print(f"----> Converting table {table_path} to {output_path} started.")

with open(allowed_tags_yaml) as file:
    allowed_tags = yaml.load(file, Loader=yaml.FullLoader)

print(f"----> Allowed tags: {', '.join(allowed_tags)}.")

tool_table = xlrd.open_workbook(table_path)
xl_sheet = tool_table.sheet_by_index(0)

num_cols = xl_sheet.ncols   # Number of columns
main_dict = {main_dict_key: []}

# Processing header
header = []
for col_idx in range(0, num_cols):
    header.append(xl_sheet.cell(0, col_idx).value)
print("----> Header parsed successfully")

# Looping over rows and adding its contents to the main dict
for row_idx in range(1, xl_sheet.nrows):
    tool = {}
    for col_idx in range(0, num_cols):
        cell_obj = xl_sheet.cell(row_idx, col_idx).value
        if cell_obj: # Only include keys if there are values
            if  header[col_idx] == 'tags':
                output = re.split(', |,', cell_obj)
                for tag in output:
                    if tag not in allowed_tags:
                        sys.exit(f'The table contains the tag "{tag}" in row {row_idx} which is not allowed.\n-> Check out the tool_tags.yaml file in the _data directory to find out the allowed tags.')
            elif header[col_idx] == 'registry':
                output={}
                for registry in re.split(', |,', cell_obj):
                    reg, identifier = re.split(':', registry)
                    if reg in allowed_registries:
                        output[reg] = identifier
                    else:
                        sys.exit(f'The table contains the registry "{reg}" in row {row_idx} which is not allowed.\n')
            else:
                output = unicodedata.normalize("NFKD", cell_obj).strip() # Return the normal form for the Unicode string
            tool[header[col_idx]] = output
    main_dict[main_dict_key].append(tool)
    print(f"{row_idx}. {tool['name']} is parsed.")

with open(output_path, 'w') as yaml_file:
    documents = yaml.dump(main_dict, yaml_file)

print("----> YAML is dumped successfully")