# !/usr/bin/python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import sys

# API call to delete an execution by ID
def delete_execution(execution_id):
    global PROPERTIES
    global HEADERS
    url = URL + 'execution/' + execution_id
    try:
        r = requests.delete(url, headers=HEADERS, verify=False, timeout=PROPERTIES['TIMEOUT'])
    except:
        pass


# API call to bulk delete executions by ID
def delete_executions():
    werte = list(range(0, 5500))
    global PROPERTIES
    global HEADERS
    url = URL + 'executions/delete'
    try:
        r = requests.post(url, headers=HEADERS, data=json.dumps({'ids': [ werte ]}), verify=False,
                          timeout=PROPERTIES['DELETE_TIMEOUT'])
    except:
        try:
            print("Problem with execution deletion {0}".format(r))
        except:
            pass
        pass

#
# Main
#
setting_filename = sys.argv[1] if len(sys.argv) > 1 else 'properties.json'
with open(setting_filename, 'r') as props_file:
    PROPERTIES = json.load(props_file)

protocol = 'http'
if PROPERTIES['SSL']:
    protocol = 'https'
    # disable warnings about unverified https connections
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

URL = '{0}://{1}:{2}/api/{3}/'.format(protocol, PROPERTIES['RUNDECKSERVER'], PROPERTIES['PORT'],
                                      PROPERTIES['API_VERSION'])
HEADERS = {'Content-Type': 'application/json', 'X-RunDeck-Auth-Token': PROPERTIES['API_KEY']}


delete_executions()
