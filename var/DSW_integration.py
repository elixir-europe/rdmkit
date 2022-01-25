import sys
import os
import re
import json
import frontmatter
from urllib.parse import urlparse
import yaml


# --------- Variables ---------
rootdir = 'pages/'
dsw_json = '/home/bedro/Downloads/dsw_root-rdmkit_2.3.7.json'


# --------- Some intresting functions ---------

def strip_end(text, suffix):
    if suffix and text.endswith(suffix):
        return text[:-len(suffix)]
    return text

# --------- Parsing DSW json ---------


with open(dsw_json) as read_file:
    data = json.load(read_file)


parent_ids = {}
titles_mapping = {}

# Parsing DSW objects with RDMkit url mention
for package in data['packages']:
    if 'events' in package:
        for event in package['events']:
            if package['kmId'] == 'root-rdmkit' and 'url' in event and 'https://rdmkit.elixir-europe.org/' in event['url']:
                parsed_url = os.path.basename(urlparse(event['url']).path)
                filename = strip_end(parsed_url, '.html')
                event_info = {}
                event_info['url'] = event['url']
                event_info['parentUuid'] = event['parentUuid']
                if filename in parent_ids:
                    parent_ids[filename].append(event_info)
                else:
                    parent_ids[filename] = [event_info]

            elif 'title' in event and 'entityUuid' in event:
                if isinstance(event['title'], str):
                    titles_mapping[event['entityUuid']] = event['title']
                elif isinstance(event['title'], dict) and 'value' in event['title'] and event['title']['value']:
                    titles_mapping[event['entityUuid']
                                   ] = event['title']['value']


# --------- Updating markdown pages with DSW links ---------


for subdir, dirs, files in os.walk(rootdir):
    for file_name in files:
        if os.path.splitext(file_name)[1] == '.md':
            filename_stripped = os.path.splitext(file_name)[0]
            with open(os.path.join(subdir, file_name), "r") as f:
                contents = f.readlines()
                frontmatter_start = False
                frontmatter_end = 0
                dsw_start = 0
                dsw_end = 0
                for index, line in enumerate(contents):
                    if re.match(r'^---', line):
                        if not frontmatter_start:
                            frontmatter_start = True
                        else:
                            frontmatter_start = False
                            frontmatter_end = index
                            if dsw_start:
                                dsw_end = index
                    elif line.startswith("dsw:") and frontmatter_start:
                        dsw_start = index
                    elif re.match(r'^[a-zA-Z]', line) and frontmatter_start and dsw_start:
                        dsw_end = index

                    if frontmatter_end:
                        break
            if ( dsw_end and dsw_start ) or filename_stripped in parent_ids:
                if  dsw_end and dsw_start:
                    del contents[dsw_start:dsw_end]
                    frontmatter_end = frontmatter_end - (dsw_end - dsw_start)
                
                metadata = {}
                if filename_stripped in parent_ids:
                    dsw_info = []
                    for dsw_object in parent_ids[filename_stripped]:
                        dsw_info.append(
                            {'name': titles_mapping[dsw_object['parentUuid']], 'parentuuid': dsw_object['parentUuid']})
                    metadata['dsw'] = dsw_info
                contents.insert(frontmatter_end, yaml.dump( metadata , default_flow_style=False))
                with open(os.path.join(subdir, file_name), "w") as f:
                    contents = "".join(contents)
                    f.write(contents)
