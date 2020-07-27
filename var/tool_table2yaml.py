import sys
import xlrd
import yaml
import re
import unicodedata

table_path = "_data/tool_list.xlsx"
output_path = "_data/tool_list.yml"
main_dict_key = "Tools"
allowed_tags_yaml = "_data/tool_tags.yml"

print(f"----> Converting table {table_path} to {output_path} started.")

with open(allowed_tags_yaml) as file:
    allowed_tags = yaml.load(file, Loader=yaml.FullLoader)['allowed-tags']

print(f"----> Allowed tags: {', '.join(allowed_tags)}.")

tool_table = xlrd.open_workbook(table_path)
xl_sheet = tool_table.sheet_by_index(0)

num_cols = xl_sheet.ncols   # Number of columns
main_dict = {main_dict_key: []}

# Prcessing header
header = []
for col_idx in range(0, num_cols):
    header.append(xl_sheet.cell(0, col_idx).value)
print("----> Header parsed successfully")

# Looping over rows and addinf its contents to the main dict
for row_idx in range(1, xl_sheet.nrows):
    tool = {}
    for col_idx in range(0, num_cols):
        cell_obj = xl_sheet.cell(row_idx, col_idx).value
        if cell_obj: # Only include keys if there are values
            if  header[col_idx] == 'tags':
                cell_obj = re.split(', |,', cell_obj)
                for tag in cell_obj:
                    if tag not in allowed_tags:
                        sys.exit(f'The table contains the tag "{tag}" in row {row_idx} which is not allowed.\n-> Check out the tool_tags.yaml file in the _data directory to find out the allowed tags.')
            else:
                cell_obj = unicodedata.normalize("NFKD", cell_obj).strip() # Return the normal form for the Unicode string
            tool[header[col_idx]] = cell_obj
    main_dict[main_dict_key].append(tool)
    print(f"{row_idx}. {tool['name']} is parsed.")

with open(output_path, 'w') as yaml_file:
    documents = yaml.dump(main_dict, yaml_file)

print("----> YAML is dumped successfully")