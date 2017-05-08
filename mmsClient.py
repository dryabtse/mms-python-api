from requests.auth import HTTPDigestAuth
import requests
import json
 
 
class MmsClient:
    def __init__(self, username, apiKey, baseUrl):
        self.username = username
        self.apiKey = apiKey
        self.url = baseUrl + '/api/public/v1.0/'
# Groups
    def getGroups(self):
        url = self.url + 'groups'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroup(self, groupId):
        url = self.url + 'groups/' + groupId
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def delGroup(self, groupId):
        url = self.url + 'groups/' + groupId
        result = requests.delete(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupUsers(self, groupId):
        url = self.url + 'groups/' + groupId + '/users'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
# Hosts
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
# Automation         
    def getAutomationConfig(self, groupId):
        url = self.url + 'groups/' + groupId + '/automationConfig'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
 
    def updateAutomationConfig(self, groupId, automationConfig):
        url = self.url + 'groups/' + groupId + '/automationConfig'
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, auth=HTTPDigestAuth(self.username, self.apiKey), json=automationConfig, headers=headers)
        return json.loads(result.text)

    def getAutomationStatus(self, groupId):
        url = self.url + 'groups/' + groupId + '/automationStatus'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
# Agents        
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
    
    def getAgentByType(self, groupId, type):
        # Todo - check the type value
        url = self.url + 'groups/' + groupId + '/agents/' + type
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getMonAgent(self, groupId):
        url = self.url + 'groups/' + groupId + '/agents/MONITORING' 
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getBakAgent(self, groupId):
        url = self.url + 'groups/' + groupId + '/agents/BACKUP' 
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getAutoAgent(self, groupId): 
        url = self.url + 'groups/' + groupId + '/agents/AUTOMATION' 
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Backup and Restore
    def getClusters(self, groupId):
        url = self.url + 'groups/' + groupId + '/clusters'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getBackupConfigs(self, groupId):
        url = self.url + 'groups/' + groupId + '/backupConfigs'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getClusterBackupConfig(self, groupId, clusterId):
        url = self.url + 'groups/' + groupId + '/backupConfigs/' + clusterId
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def patchClusterBackupConfig(self, groupId, clusterId, payload):
        url = self.url + 'groups/' + groupId + '/backupConfigs/' + clusterId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getClusterSnapshots(self, groupId, clusterId):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId + '/snapshots'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getClusterSnapshotById(self, groupId, clusterId, snapshotId):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId + '/snapshots/' + snapshotId
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getHostSnapshots(self, groupId, hostId):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/snapshots'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getHostSnapshotById(self, groupId, hostId, snapshotId):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/snapshots/' + snapshotId
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postClusterRestoreJob(self, groupId, clusterId, payload):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId + '/restoreJobs'
        result = requests.post(url, auth=HTTPDigestAuth(self.username, self.apiKey), json=payload)
        return json.loads(result.text)

    def getClusterRestoreJobs(self, groupId, clusterId):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId + '/restoreJobs'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getClusterSnapshotSchedule(self, groupId, clusterId):
        url = self.url + 'groups/' + groupId + '/backupConfigs/' + clusterId + '/snapshotSchedule'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
 
    def patchClusterSnapshotSchedule(self, groupId, clusterId, payload):
        url = self.url + 'groups/' + groupId + '/backupConfigs/' + clusterId + '/snapshotSchedule'
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)