import os
import re
from urllib.parse import urlparse
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import collections
from typing import Dict, List
import yaml


# --------- Variables ---------
rootdir = 'pages/'
DSWQuestion = collections.namedtuple('DSWQuestion', 'uuid, text')
RDMKIT_PREFIX = 'https://rdmkit.elixir-europe.org'
DSW_API_URL = 'https://api-researchers.ds-wizard.org'
DSW_KM_ID = 'dsw:root:latest'

# --------- Functions ---------

def strip_end(text, suffix):
    if suffix and text.endswith(suffix):
        return text[:-len(suffix)]
    return text

def rdmkit_page_id(url: str) -> str:
    parsed_url = os.path.basename(urlparse(url).path)
    return strip_end(parsed_url, '.html')


def client(url, payload):
    """API object fetcher"""
    print(f"POST request with url= {url} and json= {payload}")
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=15)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    r = session.post(url, json=payload)
    r.raise_for_status()
    return r.json()


def fetch_rdmkit_dsw_links(endpoint: str, package: str) -> Dict[str, List[DSWQuestion]]:
    km = client(f'{endpoint}/knowledge-models/preview', {'packageId': package, 'events': [], 'tagUuids': []})
    print(f"Parsing DSW objects with {endpoint} mention")
    links = {}  # type: dict[str, list[DSWQuestion]]
    rdmkit_references = {
        ref_id: ref for ref_id, ref in km['entities']['references'].items()
        if ref.get('url', '').startswith(RDMKIT_PREFIX)
    }
    for question_id, question in km['entities']['questions'].items():
        rdmkit_refs = (ref for ref in question['referenceUuids']
                       if ref in rdmkit_references.keys())
        for ref in rdmkit_refs:
            page_id = rdmkit_page_id(rdmkit_references[ref]['url'])
            if page_id not in links.keys():
                links[page_id] = []
            links[page_id].append(
                DSWQuestion(question_id, question['title'])
            )
    print("Done")
    return links


# --------- Parsing DSW json ---------
parent_ids = fetch_rdmkit_dsw_links(
    endpoint=DSW_API_URL,
    package=DSW_KM_ID,
)


# --------- Updating markdown pages with DSW links ---------

print(f"Updating markdown pages with DSW links")
for subdir, dirs, files in os.walk(rootdir):
    for file_name in files:
        if os.path.splitext(file_name)[1] == '.md':
            filename_stripped = os.path.splitext(file_name)[0]
            with open(os.path.join(subdir, file_name), "r") as f:
                print(f"Reading out {filename_stripped}")
                contents = f.readlines()
                frontmatter_start = False
                frontmatter_end = 0
                dsw_start = 0
                dsw_end = 0
                for index, line in enumerate(contents):
                    if re.match(r'^---', line):
                        if isinstance(frontmatter_start, bool):
                            frontmatter_start = index
                        else:
                            frontmatter_end = index
                            if dsw_start and not dsw_end:
                                dsw_end = index
                    elif line.startswith("dsw:") and isinstance(frontmatter_start, int):
                        dsw_start = index
                    elif re.match(r'^[a-zA-Z]', line) and isinstance(frontmatter_start, int) and dsw_start and not dsw_end :
                        dsw_end = index
                    if frontmatter_end:
                        print(f"\tFrontmatter present from line {frontmatter_start} - {frontmatter_end}")
                        break
            if ( dsw_end and dsw_start ) or filename_stripped in parent_ids:
                if  dsw_end and dsw_start:
                    print(f"\tdsw block present from line {dsw_start} - {dsw_end}")
                    del contents[dsw_start:dsw_end]
                    print(f"\tdsw block deleted")
                    frontmatter_end = frontmatter_end - (dsw_end - dsw_start)
                metadata = {}
                if filename_stripped in parent_ids:
                    print(f"\tMaking new frontmatter block")
                    dsw_info = []
                    for question in parent_ids[filename_stripped]:
                        dsw_info.append(
                            {'name': question.text, 'uuid': question.uuid})
                    metadata['dsw'] = dsw_info
                contents.insert(frontmatter_end, yaml.dump( metadata , default_flow_style=False))
                print(f"\tNew frontmatter block inserted in content")
                print(f"\tDumping content in markdown file {os.path.join(subdir, file_name)}")
                with open(os.path.join(subdir, file_name), "w") as f:
                    contents = "".join(contents)
                    f.write(contents)
                print(f"\tDone")
print(f"DSW links successfully added to the markdown pages")
