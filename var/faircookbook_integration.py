import os
import frontmatter
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
                print(f"Reading... {filename_stripped}")
                page = frontmatter.load(f)
                page_content = page.content
                page_metadata = page.metadata
            if 'faircookbook' in page_metadata:
                print(f"\tfaircookbook block present")
                del page_metadata['faircookbook']
                print(f"\tfaircookbook block deleted")
            for rdmkit_page in map_dict:
                if filename_stripped == rdmkit_page['rdmkit_filename']:
                    print(f"\tMaking new frontmatter block")
                    fcb_info = []
                    for recipe in rdmkit_page['links']:
                        fcb_info.append(
                            {'name': recipe['fcb_title'], 'url': f'https://w3id.org/faircookbook/{recipe["fcb_id"]}'})
                    page_metadata['faircookbook'] = fcb_info
                    page.metadata = page_metadata
                
                    print(f"\tDumping content in markdown file {os.path.join(subdir, file_name)}")
                    with open(os.path.join(subdir, file_name), "w") as f:
                        f.write(frontmatter.dumps(page) + '\n')
                        print(f"\tDone")
print(f"FCB links successfully added to the markdown pages")
