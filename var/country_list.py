import yaml
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
    try:
        r = session.get(url)
    except:
        print("Could not connect")
    if r.status_code == requests.codes.ok:
        return r.json()

def fetch_country_list():
    json_output = client(
        f"https://restcountries.com/v2/all")
    if json_output:
        return json_output
    else:
        print("Country lookup is skipped")
        exit()


# --------- Variables ---------

output_path = "_data/countries.yml"

# --------- Reading out page_ids from pages ---------

print(f"----> Fetching list of countries")
country_list = fetch_country_list()

print(f"----> Fetching country name based on country ID")
countries = {}

for country in country_list:
    if country['name'] and country['alpha2Code']:
        countries[country['alpha2Code']] = country['name']


with open(output_path, 'w') as yaml_file:
    documents = yaml.dump(countries, yaml_file)

print("----> YAML is dumped successfully")
