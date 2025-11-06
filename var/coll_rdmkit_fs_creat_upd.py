import requests
import yaml
import json
import csv
from datetime import date
import argparse

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

def return_fs_doi(m):
    doi = None
    if 'registry' in m:
        if 'fairsharing' in m['registry']:
            if m['registry']['fairsharing'] != "NA":
                doi = m['registry']['fairsharing']
    return doi

def is_record_collected(linked_records, id_to_check):
    for i in linked_records:
        if i['linked_record_id'] == id_to_check and i['relation'] == "collects":
            return True
    return False


#The format of each line of the file rdmkit_fairsharing_record_map.csv is
# URL_rdmkit_file,FAIRsharing_record_collection_id
# URL_rdmkit_file is the URL of the rdm .md file, e.g. https://raw.githubusercontent.com/elixir-europe/rdmkit/refs/heads/master/pages/your_domain/plant_sciences.md
# FAIRsharing_record_collection_id is the ID (number) of the FAIRsharing collection. If this field is empty, a collection will be created
collections_to_check = {}
existing_collection = []
with open('_data/rdmkit_fairsharing_record_map.csv', 'r', encoding='utf8') as f:
    read_csv = csv.reader(f, delimiter=",")
    for line in read_csv:
        collections_to_check[line[0]] = {}
        collections_to_check[line[0]]['record'] = None
        collections_to_check[line[0]]['record_id'] = None
        collections_to_check[line[0]]['tools'] = []
        collections_to_check[line[0]]['repeated_id'] = None

        if line[1] is not None and len(line[1].strip()) > 1:
            id = int(line[1])
            existing_collection.append(id)
            collections_to_check[line[0]]['record_id'] = id
            collections_to_check[line[0]]['new_name'] = None
        else:
            label = line[0].split('/')[-1].split('.')[0]
            collections_to_check[line[0]]['domain'] = label.replace('_',' ')
            collections_to_check[line[0]]['new_name'] = 'RDMkit '+label.replace('_',' ').title()+ ' Domain'
            collections_to_check[line[0]]['new_homepage'] = 'https://rdmkit.elixir-europe.org/'+label
            collections_to_check[line[0]]['new_ref_url'] = 'https://github.com/elixir-europe/rdmkit/blob/master/pages/your_domain/'+label+'.md'

#Instructions to connect to the API, select the real one (api.fairsharing) or the dev one (dev-api.fairsharing.org)
#url_base = "https://api.fairsharing.org/" # FAIRsharing PRODUCTION API
url_base = "https://dev-api.fairsharing.org/" # FAIRsharing DEV API

payload = "{\"user\": {\"login\":\"" + args.username + \
    "\",\"password\":\"" + args.password + "\"} }"
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url_base+"users/sign_in", headers=headers, data=payload)
data = response.json()
jwt = data['jwt']
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': "Bearer {0}".format(jwt),
}
user_id = data['id']
user_name = data['username']
doi_to_id = {}
all_records_name_url_id = {}

collec_lab_id = -1
response = requests.request("GET", url_base+"record_association_labels", headers=headers)
if response.ok:
    record_association_labels = json.loads(response.text)
    for i in record_association_labels:
        if i['name'] == 'collects':
            collec_lab_id = i['id']
            break
    if collec_lab_id == -1:
        print('Error as the collection relation ID is not found')
else:
    print('Error')
    print(response.text)




all_tools = []
for c in collections_to_check:
#Obtaining the .md file from the Github repository and check for tools inside the .md text
    r = requests.get(c)
    prev_word = ''
    to_save = False
    for word in r.text.split():
        if to_save:
            if word.replace('"','') not in collections_to_check[c]['tools']:
                t = word.replace('"','')
                collections_to_check[c]['tools'].append(t)
                if t not in all_tools:
                    all_tools.append(t)
            to_save = False
        if word == 'tool' and'{%' in prev_word:
            to_save = True
        prev_word = word


#Obtaining the .yml file with rdmkit list and check for matches between previous tools and the list
yaml_list = requests.get('https://raw.githubusercontent.com/elixir-europe/rdmkit/refs/heads/master/_data/tool_and_resource_list.yml')
data_list = yaml.load(yaml_list.text, Loader=yaml.SafeLoader)

matched_items = {}
for t in all_tools:
    for item in data_list:
        if item["id"] == t:
            matched_items[t] = {}
            matched_items[t]['rdm'] = item
            matched_items[t]['id_fs'] = None
            break


#For the existing tools in the list get the FAIRsharing ID
# if they a have a DOI in RDMKIt


for m in matched_items:
    fs_doi = return_fs_doi(matched_items[m]['rdm'])
    if fs_doi is not None:
        if fs_doi not in doi_to_id:
            #Getting the ID of the existing tool in FAIRsharing to create relation later
            response = requests.request("GET", "https://api.fairsharing.org/content_negotiation/json/FAIRsharing." +fs_doi, headers=headers)
            if response.ok:
                data = json.loads(response.text)
                doi_to_id[fs_doi] = int(data['id'])
            else:
                print("Error")
                print(response.text)
                break
        matched_items[m]['id_fs'] = doi_to_id[fs_doi]

# All new created collections in FAIRsharing are having subject life science and taxonomy "not applicable"
subject_ids_to_add = []
response = requests.request("POST",  url_base+'search/subjects?q=life science', headers=headers)
if response.ok:
    data = json.loads(response.text)['data']
    for d in data:
        if d['label'].lower() == 'life science':
            subject_ids_to_add.append(d['id'])
            break
else:
    print("Error")
    print(response.text)

taxon_ids_to_add = []
response = requests.request("POST",  url_base+'search/taxonomies?q=not applicable', headers=headers)
if response.ok:
    data = json.loads(response.text)
    for d in data:
        if d['label'].lower() == 'not applicable':
            taxon_ids_to_add.append(d['id'])
            break
else:
    print("Error")
    print(response.text)


for c in collections_to_check:
    if collections_to_check[c]['record_id'] is None:
#We assume the collection does not exist in FAIRsharing
        print('Performing actions for the URL '+c)
        #A new record needs to create in FAIRsharing including the links to the tools with dois
        new_record = {}
        new_record['fairsharing_record'] = {}
        new_record['fairsharing_record']['is_data_set'] = False
        new_record['fairsharing_record']['dups_suspected'] = False
        new_record['fairsharing_record']['record_type_id'] = 15
        new_record['fairsharing_record']['country_ids'] = []
        new_record['fairsharing_record']['metadata'] = {}
        new_record['fairsharing_record']['metadata']['name'] = collections_to_check[c]['new_name']
        new_record['fairsharing_record']['metadata']['homepage'] = collections_to_check[c]['new_homepage']
        new_record['fairsharing_record']['metadata']['reference_url'] = collections_to_check[c]['new_ref_url']
        new_record['fairsharing_record']['metadata']['year_creation'] = date.today().year
        new_record['fairsharing_record']['metadata']['description'] = 'This collection has been created via a collaboration between FAIRsharing and RDMkit to provide a live representation of those standards and databases described within the '+ collections_to_check[c]['domain']+ ' domain pages of RDMKit.'
        new_record['fairsharing_record']['metadata']['status'] = 'ready'
        new_record['fairsharing_record']['maintainers'] = []
        maint = {}
        maint['username'] = user_name
        maint['id'] = user_id
        new_record['fairsharing_record']['maintainers'].append(maint)
        new_record['fairsharing_record']['metadata']['contacts'] = []
        contact = {}
        contact['contact_name'] = 'RDMKit Editors'
        contact['contact_email'] = 'rdm-editors@elixir-europe.org'
        new_record['fairsharing_record']['metadata']['contacts'] = []
        new_record['fairsharing_record']['metadata']['contacts'].append(contact)
        new_record['fairsharing_record']['subject_ids'] = subject_ids_to_add
        new_record['fairsharing_record']['taxonomy_ids'] = taxon_ids_to_add

        json_object = json.dumps(new_record, indent=4)
        #print(json_object)
        response = requests.request("POST", url_base+'fairsharing_records', headers=headers, data=json_object)
        #print(response.text)
        if not response.ok:
            print("Error")
            print(response.text)
            break
        data = json.loads(response.text)['data']
        collections_to_check[c]['record'] = data
        collections_to_check[c]['record']['linked_records'] = []
        collections_to_check[c]['record_id'] = data['id']
        print('New record has been successfully created: record id is '+data['id'])

        #Create organisationlink
        organisation_link = {'organisation_link': {}}
        organisation_link['organisation_link']['fairsharing_record_id'] = collections_to_check[c]['record_id']
        organisation_link['organisation_link']['organisation_id'] = 841
        organisation_link['organisation_link']['relation'] = 'collaborates_on'
        json_object = json.dumps(organisation_link, indent=4)
        response = requests.request("POST", url_base+'organisation_links', headers=headers, data=json_object)
        organisation_link['organisation_link']['organisation_id'] = 4764
        organisation_link['organisation_link']['relation'] = 'maintains'
        organisation_link['organisation_link']['is_lead'] = True
        json_object = json.dumps(organisation_link, indent=4)
        response = requests.request("POST", url_base+'organisation_links', headers=headers, data=json_object)
    else:
##We assume the collection exists in FAIRsharing        
        response = requests.request("GET", url_base + "fairsharing_records/" +str(collections_to_check[c]['record_id']), headers=headers)
        if response.ok:
            collections_to_check[c]['record'] = json.loads(response.text)['data']['attributes']
        else:
            print('Error')
            print(response.text)


    tools_id_to_add = []
    for t in collections_to_check[c]['tools']:
        if matched_items[t]['id_fs'] is not None:
            tools_id_to_add.append(matched_items[t]['id_fs'])

    #Check if there are existing relations in FAIRsharing that are not longer appear in the RDMKit
    #If so, we need to delete it
    for link_rec in collections_to_check[c]['record']['linked_records']:
        if link_rec['linked_record_id'] not in tools_id_to_add:
           response = requests.request("DELETE", url_base+'record_associations/'+str(link_rec['link_id']), headers=headers)
           if response.ok:
               print('In the FAIRsharing collection '+str(collections_to_check[c]['record_id'])+' the relation with the record '+str(link_rec['linked_record_id'])+' is removed.')
           else:
               print("Error")
               print(response.text)
    #Create relations between the collection and tools that existed in FAIRshsaring and not already exist
    num_relations = 0
    for id_rec in tools_id_to_add:
        if not is_record_collected(collections_to_check[c]['record']['linked_records'],id_rec):
            record_association = {'record_association': {}}
            record_association['record_association']['fairsharing_record_id'] = collections_to_check[c]['record_id']
            record_association['record_association']['linked_record_id'] = id_rec
            record_association['record_association']['record_assoc_label_id'] = collec_lab_id
            json_object = json.dumps(record_association, indent=4)
            response = requests.request("POST", url_base+'record_associations', headers=headers, data=json_object)
            if response.ok:
                num_relations += 1
            else:
                print("Error")
                print(response.text)
    print('For the record '+str(collections_to_check[c]['record_id'])+' '+str(num_relations)+' records are collected')
