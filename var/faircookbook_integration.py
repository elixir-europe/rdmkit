import os
import re
import yaml
import sys


# --------- Variables ---------
rootdir = 'pages/'
map_file = sys.argv[1]

# --------- Functions ---------

def strip_end(text, suffix):
    if suffix and text.endswith(suffix):
        return text[:-len(suffix)]
    return text


# --------- Parsing mapping file ---------


with open(map_file, 'r') as stream:
    map_dict = yaml.safe_load(stream)

# --------- Updating markdown pages with FAIR Cookbook links ---------

print(f"Updating markdown pages with FAIR Cookbook links")
for subdir, dirs, files in os.walk(rootdir):
    for file_name in files:
        if os.path.splitext(file_name)[1] == '.md':
            filename_stripped = os.path.splitext(file_name)[0]
            with open(os.path.join(subdir, file_name), "r") as f:
                print(f"Reading out {filename_stripped}")
                contents = f.readlines()
                frontmatter_start = False
                frontmatter_end = 0
                fcb_start = 0
                fcb_end = 0
                for index, line in enumerate(contents):
                    if re.match(r'^---', line):
                        if isinstance(frontmatter_start, bool):
                            frontmatter_start = index
                        else:
                            frontmatter_end = index
                            if fcb_start and not fcb_end:
                                fcb_end = index
                    elif line.startswith("faircookbook:") and isinstance(frontmatter_start, int):
                        fcb_start = index
                    elif re.match(r'^[a-zA-Z]', line) and isinstance(frontmatter_start, int) and fcb_start and not fcb_end :
                        fcb_end = index
                    if frontmatter_end:
                        print(f"\tFrontmatter present from line {frontmatter_start} - {frontmatter_end}")
                        break
            if  fcb_end and fcb_start:
                print(f"\tfcb block present from line {fcb_start} - {fcb_end}")
                del contents[fcb_start:fcb_end]
                print(f"\tfcb block deleted")
                frontmatter_end = frontmatter_end - (fcb_end - fcb_start)
            for rdmkit_page in map_dict:
                metadata = {}
                if filename_stripped == rdmkit_page['rdmkit_filename']:
                    print(f"\tMaking new frontmatter block")
                    fcb_info = []
                    for recipe in rdmkit_page['links']:
                        fcb_info.append(
                            {'name': recipe['fcb_title'], 'url': f'https://w3id.org/faircookbook/{recipe["fcb_id"]}'})
                    metadata['faircookbook'] = fcb_info
                    contents.insert(frontmatter_end, yaml.dump( metadata , default_flow_style=False))
                    print(f"\tNew frontmatter block inserted in content")
                    print(f"\tDumping content in markdown file {os.path.join(subdir, file_name)}")
                    with open(os.path.join(subdir, file_name), "w") as f:
                        contents = "".join(contents)
                        f.write(contents)
                    print(f"\tDone")
print(f"FCB links successfully added to the markdown pages")
