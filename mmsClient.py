from requests.auth import HTTPDigestAuth
import requests
import json
 
 
class MmsClient:
    def __init__(self, username, apiKey, baseUrl):
        self.username = username
        self.apiKey = apiKey
        self.url = baseUrl + '/api/public/v1.0/'
 
    def getAutomationConfig(self, groupId):
        url = self.url + 'groups/' + groupId + '/automationConfig'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
        
    def getHosts(self, groupId):
        url = self.url + 'groups/' + groupId + '/hosts'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getHostByNameAndPort(self, groupId, hostname, port):
        url = self.url + 'groups/' + groupId + '/hosts/byName/' + hostname + ':' + port
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def delHost(self, groupId, hostId):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId
        result = requests.delete(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
 
    def updateAutomationConfig(self, groupId, automationConfig):
        url = self.url + 'groups/' + groupId + '/automationConfig'
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, auth=HTTPDigestAuth(self.username, self.apiKey), json=automationConfig, headers=headers)
        return json.loads(result.text)
        
    def putMonAgentInfo(self, groupId, agentConfig):
        url = self.url + 'groups/' + groupId + '/automationConfig/monitoringAgentConfig' 
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, auth=HTTPDigestAuth(self.username, self.apiKey), json=agentConfig, headers=headers)
        return json.loads(result.text)
        
    def putBackAgentInfo(self, groupId, agentConfig):
        url = self.url + 'groups/' + groupId + '/automationConfig/backupAgentConfig' 
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, auth=HTTPDigestAuth(self.username, self.apiKey), json=agentConfig, headers=headers)
        return json.loads(result.text)
    
    def getAgents(self, groupId):
        url = self.url + 'groups/' + groupId + '/agents'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def agentByType(self, groupId, type):
        # Todo - check the type value
        url = self.url + 'groups/' + groupId + '/agents/' + type
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
 

username = ""
apiKey = ""
baseUrl = ""
mmsClient = MmsClient(username, apiKey, baseUrl)

groupId = ""


##### Main section
automationConfig = mmsClient.getAutomationConfig(groupId)
print(json.dumps(automationConfig["version"]))

#To remove a node from replica set:
#
#del automationConfig["processes"][2]["args2_6"]["replication"]
#automationConfig["replicaSets"][0]["members"].pop(2)
#automationConfig["version"] = int(automationConfig["version"]) + 1
#updateResult = mmsClient.updateAutomationConfig(groupId, automationConfig)
#print(json.dumps(updateResult))

#f( len(automationConfig["processes"]) > 0):
   # automationConfig["processes"][0]["disabled"] = True
    #automationConfig["version"] = int(automationConfig["version"]) + 1
    #updateResult = mmsClient.updateAutomationConfig(groupId, automationConfig)
    #print(json.dumps(updateResult))

hosts = mmsClient.getHosts(groupId)
for host in hosts["results"]:
    print(json.dumps(host["id"]))
    print(json.dumps(host["hostname"]))
    print(json.dumps(host["port"]))

mmsClient.delHost(groupId, id)

hostname = ""
port = "27015"

host = mmsClient.getHostByNameAndPort(groupId, hostname, port)


# To stop a process 
# automationConfig["processes"][5]["disabled"] = True
