# mms-python-api

A Python class that exposes most of the REST API endpoints provided by MongoDB Cloud Manager / Ops Manager / Atlas.

## Example
```
import json
import sys
from mmsClient import MmsClient

def jsonPrintPretty(json_doc):
    print json.dumps(json_doc, sort_keys=True, indent=4, separators=(',', ': '))

username = "vaudeville.villain"
apiKey = "6f64db12-5401-40db-afbe-8f522377705d"
baseUrl = "http://dmn-opsmanager:8080"
mmsClient = MmsClient(username, apiKey, baseUrl)

groupId = "5893fcfbbdbb57293a871dc8"

clusters = mmsClient.getClusters(groupId)

jsonPrintPretty(clusters)
```
