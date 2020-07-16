from requests.auth import HTTPDigestAuth
import requests
import json
 
 
class MmsClient:
    def __init__(self, username, apiKey, baseUrl, verify=False):
        self.username = username
        self.apiKey = apiKey
        self.url = baseUrl + '/api/public/v1.0/'
        self.atlasUrl = baseUrl + '/api/atlas/v1.0/'
        self.verify = verify

# Root

    def getRoot(self, pageNum=None, itemsPerPage=100, envelope=False):
        url = self.url + '?itemsPerPage=' + str(itemsPerPage) + '&envelope=' + str(envelope)
        if (pageNum is not None):
            url = url + '&pageNume=' + str(pageNum) 
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Groups

    def getGroups(self, pageNum=None, itemsPerPage=100, pretty=False):
        url = self.url + 'groups?itemsPerPage=' + str(itemsPerPage) + '&pretty=' + str(pretty)
        if (pageNum is not None):
            url = url + '&pageNume=' + str(pageNum) 
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroup(self, groupId):
        url = self.url + 'groups/' + groupId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupByGroupName(self, groupId, groupName):
        url = self.url + 'groups/byName' + groupName
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupByAgentApiKey(self, groupId, agentApiKey):
        url = self.url + 'groups/byAgentApiKey' + agentApiKey
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postGroup(self, group):
        url = self.url + 'groups'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=group, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def postGroupUser(self, groupId, user):
        url = self.url + 'groups/' + groupId + '/users'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=user, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def patchGroup(self, groupId, payload):
        url = self.url + 'groups/' + groupId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delGroup(self, groupId):
        url = self.url + 'groups/' + groupId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupUsers(self, groupId):
        url = self.url + 'groups/' + groupId + '/users'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def delGroupUser(self, groupId, userId):
        url = self.url + 'groups/' + groupId + '/users/' + userId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupByTags(self, groupId, tags):
        url = self.url + 'groups/?'
        
        if (isinstance(tags, str)):
            url = url + 'tags=' + tags
        else:
            try:
                i = 0
                for tag in tags:
                    if ( i > 0 ):
                        url = url + '&'
                    url = url + 'tag=' + tag
                    i = i + 1
            except TypeError:
                return { 'Error': '\'tags\' is expected to be a string or a list' }

        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Users

    def getUserByUserId(self, userId):
        url = self.url + 'users/' + userId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getUserByUserName(self, userName):
        url = self.url + 'users/' + userName
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def postUser(self, user):
        url = self.url + 'users'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=user, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def postFirstUser(self, user):
        url = self.url + 'unauth/users'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=user, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def patchUser(self, userId, payload):
        url = self.url + 'users/' + userId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

# Whitelist

    def getWhitelist(self, userId):
        url = self.url + 'users/' + userId + '/whitelist'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getWhitelistByIpAddress(self, userId, ipAddress):
        # TODO handle CIDR blocks if passed instead of IP Address
        url = self.url + 'users/' + userId + '/whitelist/' + ipAddress
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postWhitelist(self, userId, whitelist):
        url = self.url + 'users/' + userId + '/whitelist'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=whitelist, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delWhitelistByIpAddress(self, userId, ipAddress):
        # TODO handle CIDR blocks if passed instead of IP Address
        url = self.url + 'users/' + userId + '/whitelist/' + ipAddress
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Hosts

    def getHosts(self, groupId):
        url = self.url + 'groups/' + groupId + '/hosts'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getHostByHostId(self, groupId, hostId):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getHostByNameAndPort(self, groupId, hostname, port):
        url = self.url + 'groups/' + groupId + '/hosts/byName/' + hostname + ':' + port
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postHost(self, groupId, host):
        url = self.url + 'groups/' + groupId + '/hosts'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=host, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def patchHost(self, groupId, hostId, payload):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delHost(self, groupId, hostId):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Disks

    def getDiskPartitions(self, groupId, hostId):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/disks'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getDiskPartitionByPartitionName(self, groupId, hostId, partitionName):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/disks/' + partitionName
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Databases

    def getDatabases(self, groupId, hostId):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/databases'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getDatabaseByDatabaseName(self, groupId, hostId, databaseName):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/databases/' + databaseName
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Clusters

    def getClusters(self, groupId):
        url = self.url + 'groups/' + groupId + '/clusters'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getClusterByClusterId(self, groupId, clusterId):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def patchCluster(self, groupId, clusterId, payload):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

# Automation         

    def getAutomationConfig(self, groupId):
        url = self.url + 'groups/' + groupId + '/automationConfig'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
 
    def putAutomationConfig(self, groupId, automationConfig):
        url = self.url + 'groups/' + groupId + '/automationConfig'
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey), json=automationConfig, headers=headers)
        return json.loads(result.text)

    def getAutomationStatus(self, groupId):
        url = self.url + 'groups/' + groupId + '/automationStatus'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Agents        

    def putMonitoringAgentConfig(self, groupId, agentConfig):
        url = self.url + 'groups/' + groupId + '/automationConfig/monitoringAgentConfig' 
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey), json=agentConfig, headers=headers)
        return json.loads(result.text)
        
    def putBackupAgentConfig(self, groupId, agentConfig):
        url = self.url + 'groups/' + groupId + '/automationConfig/backupAgentConfig' 
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey), json=agentConfig, headers=headers)
        return json.loads(result.text)

    def postUpdateAgentVersions(self, groupId):
        url = self.url + 'groups/' + groupId + '/automationConfig/updateAgentVersions'
        headers = {'Accept': 'application/json'}
        result = requests.post(url, verify=self.verify, json={}, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getAgents(self, groupId):
        url = self.url + 'groups/' + groupId + '/agents'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getAgentByType(self, groupId, type):
        # Todo - check the type value
        url = self.url + 'groups/' + groupId + '/agents/' + type
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getMonitoringAgent(self, groupId):
        url = self.url + 'groups/' + groupId + '/agents/MONITORING' 
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getBackupAgent(self, groupId):
        url = self.url + 'groups/' + groupId + '/agents/BACKUP' 
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getAutomationAgent(self, groupId): 
        url = self.url + 'groups/' + groupId + '/agents/AUTOMATION' 
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)



# Backup and Restore
    
    def getBackupConfigs(self, groupId):
        url = self.url + 'groups/' + groupId + '/backupConfigs'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getClusterBackupConfig(self, groupId, clusterId):
        url = self.url + 'groups/' + groupId + '/backupConfigs/' + clusterId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def patchClusterBackupConfig(self, groupId, clusterId, payload):
        url = self.url + 'groups/' + groupId + '/backupConfigs/' + clusterId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getClusterSnapshots(self, groupId, clusterId):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId + '/snapshots'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getClusterSnapshotBySnapshotId(self, groupId, clusterId, snapshotId):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId + '/snapshots/' + snapshotId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getHostSnapshots(self, groupId, hostId):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/snapshots'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getHostSnapshotBySnapshotId(self, groupId, hostId, snapshotId):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/snapshots/' + snapshotId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    # Backup Encryption Keys

    def putClusterEncryptionKey(self, groupId, clusterId, encryptionKey):
        url = self.url + 'groups/' + groupId + '/backupConfigs/' + clusterId + '/encryptionKey'
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, verify=self.verify, json=encryptionKey, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getClusterEncryptionKey(self, groupId, clusterId):
        url = self.url + 'groups/' + groupId + '/backupConfigs/' + clusterId + '/encryptionKey'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    # Restore Jobs

    def getClusterRestoreJobs(self, groupId, clusterId, batchId=None):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId + '/restoreJobs'
        if (batchId is not None):
            url = url + '?batchId=' + batchId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getClusterRestoreJobByRestoreJobId(self, groupId, clusterId, restoreJobId):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId + '/restoreJobs/' + restoreJobId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getHostRestoreJobs(self, groupId, hostId):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/restoreJobs'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getHostRestoreJobByRestoreJobId(self, groupId, hostId, restoreJobId):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/restoreJobs' + restoreJobId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postClusterRestoreJob(self, groupId, clusterId, restoreJob):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId + '/restoreJobs'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=restoreJob, auth=HTTPDigestAuth(self.username, self.apiKey),  headers=headers)
        return json.loads(result.text)

    def postHostRestoreJob(self, groupId, hostId, restoreJob):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/restoreJobs'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=restoreJob, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    # Snapshot Schedule

    def getClusterSnapshotSchedule(self, groupId, clusterId):
        url = self.url + 'groups/' + groupId + '/backupConfigs/' + clusterId + '/snapshotSchedule'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
 
    def patchClusterSnapshotSchedule(self, groupId, clusterId, payload):
        url = self.url + 'groups/' + groupId + '/backupConfigs/' + clusterId + '/snapshotSchedule'
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    # Checkpoints

    def getClusterCheckpoints(self, groupId, clusterId):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId + '/checkpoints'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getClusterCheckpointsByCheckpointId(self, groupId, clusterId, checkpointId):
        url = self.url + 'groups/' + groupId + '/clusters/' + clusterId + '/checkpoints/' + checkpointId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Alerts

    def getAlerts(self, groupId):
        url = self.url + 'groups/' + groupId + '/alerts'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getAlertById(self, groupId, alertId):
        url = self.url + 'groups/' + groupId + '/alerts/' + alertId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def patchAlert(self, groupId, alertId, payload):
        url = self.url + 'groups/' + groupId + '/alerts/' + alertId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getAlertConfig(self, groupId):
        url = self.url + 'groups/' + groupId + '/alertConfigs'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postAlertConfig(self, groupId, alertConfig):
        url = self.url + 'groups/' + groupId + '/alertConfigs'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=alertConfig, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getAlertConfigById(self, groupId, alertConfigId):
        url = self.url + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def putAlertConfig(self, groupId, alertConfigId, alertConfig):
        url = self.url + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey), json=alertConfig, headers=headers)
        return json.loads(result.text)

    def patchAlertConfig(self, groupId, alertConfigId, payload):
        url = self.url + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delAlertConfig(self, groupId, alertConfigId):
        url = self.url + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getAlertsByAlertConfigId(self, groupId, alertConfigId):
        url = self.url + 'groups/' + groupId + '/alertConfigs/' + alertConfigId + '/alerts'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
# Global alerts

    def getGlobalAlerts(self, status=None):
        url = self.url + 'globalAlerts'
        if (status):
            url = url + '?status=' + status
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getGlobalAlertById(self, globalAlertId):
        url = self.url + 'globalAlerts/' + globalAlertId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def patchGlobalAlert(self, globalAlertId, payload):
        url = self.url + 'globalAlerts/' + globalAlertId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getGlobalAlertConfigs(self):
        url = self.url + 'globalAlertConfigs'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getGlobalAlertConfigById(self, globalAlertConfigId):
        url = self.url + 'globalAlertConfigs/' + globalAlertConfigId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getAlertsByGlobalAlertConfigId(self, globalAlertConfigId):
        url = self.url + 'globalAlertConfigs/' + globalAlertConfigId + '/alerts'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def postGlobalAlertConfig(self, globalAlertConfig):
        url = self.url + 'globalAlertConfigs'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=globalAlertConfig, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)
    
    def putGlobalAlertConfig(self, globalAlertConfigId, globalAlertConfig):
        url = self.url + 'globalAlertConfigs/' + globalAlertConfigId
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey), json=globalAlertConfig, headers=headers)
        return json.loads(result.text)

    def patchGlobalAlertConfig(self, globalAlertConfigId, payload):
        url = self.url + 'globalAlertConfigs/' + globalAlertConfigId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delGlobalAlertConfig(self, globalAlertConfigId):
        url = self.url + 'globalAlertConfigs/' + globalAlertConfigId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Maintenance windows

    def getMaintenanceWindows(self, groupId):
        url = self.url + 'groups/' + groupId + '/maintenanceWindows'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getMaintenanceWindowById(self, groupId, maintenanceWindowId):
        url = self.url + 'groups/' + groupId + '/maintenanceWindows/' + maintenanceWindowId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postMaintenanceWindow(self, groupId, maintenanceWindow):
        url = self.url + 'groups/' + groupId + '/maintenanceWindows'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=maintenanceWindow, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def patchMaintenanceWindow(self, groupId, maintenanceWindowId, payload):
        url = self.url + 'groups/' + groupId + '/maintenanceWindows/' + maintenanceWindowId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delMaintenanceWindow(self, groupId, maintenanceWindowId):
        url = self.url + 'groups/' + groupId + '/maintenanceWindows/' + maintenanceWindowId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Measurements

    def getHostMeasurements(self, groupId, hostId, granularity, measurements=None, period=None, start=None, end=None):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/measurements?granularity=' + granularity
        
        if not (measurements is None):
            if (isinstance(measurements, str)):
                url = url + '&m=' + measurements
            else:
                try:
                    for m in measurements:
                        url = url + '&m=' + m
                except TypeError:
                    return { 'Error': '\'measurement\' is expected to be a string or a list' }

        if (period is not None):
            url = url + '&period=' + period
        else:
            if((start is not None) and (end is not None)):
                url = url + '&start=' + start + '&end=' + end
            else:
                return { 'Error': 'This endpoint requires either \'period\' or \'start\' & \'end\' parameters to be passed on' }
        
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getDiskPartitionMeasurements(self, groupId, hostId, partitionName, granularity, measurements=None, period=None, start=None, end=None):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/disks/' + partitionName +'/measurements?granularity=' + granularity
        
        if not (measurements is None):
            if (isinstance(measurements, str)):
                url = url + '&m=' + measurements
            else:
                try:
                    for m in measurements:
                        url = url + '&m=' + m
                except TypeError:
                    return { 'Error': '\'measurement\' is expected to be a string or a list' }

        if (period is not None):
            url = url + '&period=' + period
        else:
            if((start is not None) and (end is not None)):
                url = url + '&start=' + start + '&end=' + end
            else:
                return { 'Error': 'This endpoint requires either \'period\' or \'start\' & \'end\' parameters to be passed on' }

        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getDatabaseMeasurements(self, groupId, hostId, databaseName, granularity, measurements=None, period=None, start=None, end=None):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/databases/' + databaseName +'/measurements?granularity=' + granularity
        
        if not (measurements is None):
            if (isinstance(measurements, str)):
                url = url + '&m=' + measurements
            else:
                try:
                    for m in measurements:
                        url = url + '&m=' + m
                except TypeError:
                    return { 'Error': '\'measurement\' is expected to be a string or a list' }

        if (period is not None):
            url = url + '&period=' + period
        else:
            if((start is not None) and (end is not None)):
                url = url + '&start=' + start + '&end=' + end
            else:
                return { 'Error': 'This endpoint requires either \'period\' or \'start\' & \'end\' parameters to be passed on' }

        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Server Pool
    
    def getServerPool(self):
        url = self.url + 'serverPool'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getServerPoolServers(self, status=None):
        url = self.url + 'serverPool/servers'
        if (status is not None):
            url = url + '?status=' + status
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getServerPoolServerByServerId(self, serverId):
        url = self.url + 'serverPool/servers/' + serverId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getServerPoolServersByHostname(self, hostname):
        url = self.url + 'serverPool/servers/byName/' + hostname
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def delServerPoolServer(self, serverId):
        url = self.url + 'serverPool/servers/' + serverId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getServerPoolRequests(self, status=None):
        url = self.url + 'serverPool/requests'
        if (status is not None):
            url = url + '?status=' + status
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getServerPoolRequestByRequestId(self, requestId):
        url = self.url + 'serverPool/requests/' + requestId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def delServerPoolRequest(self, requestId):
        url = self.url + 'serverPool/requests/' + requestId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getServerPoolProperties(self):
        url = self.url + 'serverPool/properties'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def patchServerPoolProperty(self, propertyId, payload):
        url = self.url + 'serverPool/properties/' + propertyId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def patchServerPoolPropertyValue(self, propertyId, valueName, payload):
        url = self.url + 'serverPool/properties/' + propertyId + '/values/' + valueName
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delServerPoolProperty(self, propertyId):
        url = self.url + 'serverPool/properties/' + propertyId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def delServerPoolPropertyValue(self, propertyId, valueName):
        url = self.url + 'serverPool/properties/' + propertyId + '/values/' + valueName
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupServerPool(self, groupId):
        url = self.url + 'groups/' + groupId + '/serverPool'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupServerPoolServers(self, groupId):
        url = self.url + 'groups/' + groupId + '/serverPool/servers'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupServerPoolServerByServerId(self, groupId, serverId):
        url = self.url + 'groups/' + groupId + '/serverPool/servers' + serverId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupServerPoolServerByHostname(self, groupId, hostname):
        url = self.url + 'groups/' + groupId + '/serverPool/servers/byName/' + hostname
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def delGroupServerPoolServer(self, groupId, serverId):
        url = self.url + 'groups/' + groupId + '/serverPool/servers' + serverId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupServerPoolRequests(self, groupId):
        url = self.url + 'groups/' + groupId + '/serverPool/requests'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupServerPoolRequestByRequestId(self, groupId, requestId):
        url = self.url + 'groups/' + groupId + '/serverPool/requests/' + requestId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postGroupServerPoolRequest(self, groupId, request):
        url = self.url + 'groups/' + groupId + '/serverPool/requests'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=request, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delGroupServerPoolRequest(self, groupId, requestId):
        url = self.url + 'groups/' + groupId + '/serverPool/requests/' + requestId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getGroupServerPoolProperties(self, groupId):
        url = self.url + 'groups/' + groupId + '/serverPool/properties'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

## ATLAS

# Group IP Whitelist

    def getAtlasGroupWhitelist(self, groupId):
        url = self.atlasUrl + 'groups/' + groupId + '/whitelist'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getAtlasGroupWhitelistEntryByIpAddress(self, groupId, ipAddress):
        # TODO handle CIDR blocks if passed instead of IP Address
        url = self.atlasUrl + 'group/' + groupId + '/whitelist/' + ipAddress
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postAtlasGroupWhitelistEntry(self, groupId, cidrBlock):
        url = self.atlasUrl + 'group/' + groupId + '/whitelist'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=cidrBlock, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delAtlasGroupWhitelistEntry(self, groupId, ipAddress):
        # TODO handle CIDR blocks if passed instead of IP Address
        url = self.atlasUrl + 'group/' + groupId + '/whitelist/' + ipAddress
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Database Users

    def getAtlasGroupDatabaseUsers(self, groupId):
        url = self.atlasUrl + 'groups/' + groupId + '/databaseUsers'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getAtlasGroupDatabaseUserByUserName(self, groupId, userName):
        url = self.atlasUrl + 'groups/' + groupId + '/databaseUsers/admin/' + userName
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postAtlasGroupDatabaseUser(self, groupId, user):
        url = self.atlasUrl + 'groups/' + groupId + '/databaseUsers'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=user, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def patchAtlasGroupDatabaseUser(self, groupId, userName, payload):
        url = self.atlasUrl + 'groups/' + groupId + '/databaseUsers/admin/' + userName
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delAtlasGroupDatabaseUser(self, groupId, userName):
        url = self.atlasUrl + 'groups/' + groupId + '/databaseUsers/admin/' + userName
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getAtlasGroupClusters(self, groupId):
        url = self.atlasUrl + 'groups/' + groupId + '/clusters'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getAtlasGroupClusterByClusterName(self, groupId, clusterName):
        url = self.atlasUrl + 'groups/' + groupId + '/clusters/' + clusterName
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postAtlasGroupCluster(self, groupId, cluster):
        url = self.atlasUrl + 'groups/' + groupId + '/clusters'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=cluster, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def patchAtlasGroupCluster(self, groupId, clusterName, payload):
        url = self.atlasUrl + 'groups/' + groupId + '/clusters/' + clusterName
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delAtalsGroupCluster(self, groupId, clusterName):
        url = self.atlasUrl + 'groups/' + groupId + '/clusters/' + clusterName
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Alerts
    
    def getAtlasGroupAlerts(self, groupId):
        url = self.atlasUrl + 'groups/' + groupId + '/alerts'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getAtlasGroupAlertByAlertId(self, groupId, alertId):
        url = self.atlasUrl + 'groups/' + groupId + '/alerts/' + alertId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def patchAtlasGroupAlert(self, groupId, alertId, payload):
        url = self.atlasUrl + 'groups/' + groupId + '/alerts/' + alertId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

# Alert Configurations

    def getAtlasGroupAlertConfigs(self, groupId):
        url = self.atlasUrl + 'groups/' + groupId + '/alertConfigs'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postAtlasGroupAlertConfig(self, groupId, alertConfig):
        url = self.atlasUrl + 'groups/' + groupId + '/alertConfigs'       
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=alertConfig, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getAltasGroupAlertConfigByAlertConfigId(self, groupId, alertConfigId):
        url = self.atlasUrl + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def putAtlasGroupAlertConfig(self, groupId, alertConfigId, alertConfig):
        url = self.atlasUrl + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, verify=self.verify, json=alertConfig, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def patchAtlasGroupAlertConfig(self, groupId, alertConfigId, payload):
        url = self.atlasUrl + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delAtalsGroupAlertConfig(self, groupId, alertConfigId):
        url = self.atlasUrl + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getAtlasGroupAlertConfigAlerts(self, groupId, alertConfigId):
        url = self.atlasUrl + 'groups/' + groupId + '/alertConfigs/' + alertConfigId + '/alerts'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# VPC

    def getAtlasGroupContainers(self, groupId):
        url = self.atlasUrl + 'groups/' + groupId + '/containers'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postAtlasGroupContainer(self, groupId, container):
        url = self.atlasUrl + 'groups/' + groupId + '/containers'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=container, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getAtlasGroupContainerByContainerId(self, groupId, containerId):
        url = self.atlasUrl + 'groups/' + groupId + '/containers/' + containerId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def patchAtlasGroupContainer(self, groupId, containerId, payload):
        url = self.atlasUrl + 'groups/' + groupId + '/containers/' + containerId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)
    
    def getAtlasGroupPeers(self, groupId):
        url = self.atlasUrl + 'groups/' + groupId + '/peers'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postAtlasGroupPeer(self, groupId, peer):
        url = self.atlasUrl + 'groups/' + groupId + '/peers'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=peer, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getAtlasGroupPeerByPeerId(self, groupId, peerId):
        url = self.atlasUrl + 'groups/' + groupId + '/peers/' + peerId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def patchAtlasGroupPeer(self, groupId, peerId, payload):
        url = self.atlasUrl + 'groups/' + groupId + '/peers/' + peerId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, verify=self.verify, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delAtlasGroupPeer(self, groupId, peerId):
        url = self.atlasUrl + 'groups/' + groupId + '/peers/' + peerId
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# User API Whitelist

    def getAtlasUserWhitelist(self, userId):
        url = self.atlasUrl + 'users/' + userId + '/whitelist'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getAltasUserWhitelistByIpAddress(self, userId, ipAddress):
        # TODO handle CIDR blocks if passed instead of IP Address
        url = self.atlasUrl + 'users/' + userId + '/whitelist/' + ipAddress
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postAtlasUserWhitelistEntry(self, userId, whitelistEntry):
        url = self.atlasUrl + 'users/' + userId + '/whitelist'
        headers = {'Content-type': 'application/json'}
        result = requests.post(url, verify=self.verify, json=whitelistEntry, auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delAtlasUserWhitelistEntry(self, userId, ipAddress):
        # TODO handle CIDR blocks if passed instead of IP Address
        url = self.atlasUrl + 'users/' + userId + '/whitelist/' + ipAddress
        result = requests.delete(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Events

    def getAtlasOrgEvents(self, orgId):
        url = self.atlasUrl + 'orgs/' + orgId + '/events'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text) 

    def getAtlasOrgEvent(self, orgId, eventId):
        url = self.atlasUrl + 'orgs/' + orgId + '/events/' + eventId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getAtlasGroupEvents(self, groupId):
        url = self.atlasUrl + 'groups/' + groupId + '/events'
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getAtlasGroupEvent(self, groupId, eventId):
        url = self.atlasUrl + 'groups/' + groupId + '/events/' + eventId
        result = requests.get(url, verify=self.verify, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text) 