from requests.auth import HTTPDigestAuth
import requests
import json
 
 
class MmsClient:
    def __init__(self, username, apiKey, baseUrl):
        self.username = username
        self.apiKey = apiKey
        self.url = baseUrl + '/api/public/v1.0/'

# Root

    def getRoot(self):
        result = requests.get(self.url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

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

# Alerts

    def getAlerts(self, groupId):
        url = self.url + 'groups/' + groupId + '/alerts'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getAlertById(self, groupId, alertId):
        url = self.url + 'groups/' + groupId + '/alerts/' + alertId
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def patchAlert(self, groupId, alertId, payload):
        url = self.url + 'groups/' + groupId + '/alerts/' + alertId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getAlertConfig(self, groupId):
        url = self.url + 'groups/' + groupId + '/alertConfigs'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postAlertConfig(self, groupId, alertConfig):
        url = self.url + 'groups/' + groupId + '/alertConfigs'
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, data=json.dumps(alertConfig), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getAlertConfigById(self, groupId, alertConfigId):
        url = self.url + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def putAlertConfig(self, groupId, alertConfigId, alertConfig):
        url = self.url + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, auth=HTTPDigestAuth(self.username, self.apiKey), json=alertConfig, headers=headers)
        return json.loads(result.text)

    def patchAlertConfig(self, groupId, alertConfigId, payload):
        url = self.url + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delAlertConfig(self, groupId, alertConfigId):
        url = self.url + 'groups/' + groupId + '/alertConfigs/' + alertConfigId
        result = requests.delete(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getAlertsByAlertConfigId(self, groupId, alertConfigId):
        url = self.url + 'groups/' + groupId + '/alertConfigs/' + alertConfigId + '/alerts'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
# Global alerts

    def getGlobalAlerts(self, status=None):
        url = self.url + 'globalAlerts'
        if (status):
            url = url + '?status=' + status
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getGlobalAlertById(self, globalAlertId):
        url = self.url + 'globalAlerts/' + globalAlertId
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def patchGlobalAlert(self, globalAlertId, payload):
        url = self.url + 'globalAlerts/' + globalAlertId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def getGlobalAlertConfigs(self):
        url = self.url + 'globalAlertConfigs'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getGlobalAlertConfigById(self, globalAlertConfigId):
        url = self.url + 'globalAlertConfigs/' + globalAlertConfigId
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getAlertsByGlobalAlertConfigId(self, globalAlertConfigId):
        url = self.url + 'globalAlertConfigs/' + globalAlertConfigId + '/alerts'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def postGlobalAlertConfig(self, globalAlertConfig):
        url = self.url + 'globalAlertConfigs'
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, data=json.dumps(globalAlertConfig), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)
    
    def putGlobalAlertConfig(self, globalAlertConfigId, globalAlertConfig):
        url = self.url + 'globalAlertConfigs/' + globalAlertConfigId
        headers = {'Content-type': 'application/json'}
        result = requests.put(url, auth=HTTPDigestAuth(self.username, self.apiKey), json=globalAlertConfig, headers=headers)
        return json.loads(result.text)

    def patchGlobalAlertConfig(self, globalAlertConfigId, payload):
        url = self.url + 'globalAlertConfigs/' + globalAlertConfigId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delGlobalAlertConfig(self, globalAlertConfig):
        url = self.url + 'globalAlertConfigs/' + globalAlertConfigId
        result = requests.delete(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Maintenance windows

    def getMaintenanceWindows(self, groupId):
        url = self.url + 'groups/' + groupId + '/maintenanceWindows'
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)
    
    def getMaintenanceWindowById(self, groupId, maintenanceWindowId):
        url = self.url + 'groups/' + groupId + '/maintenanceWindows/' + maintenanceWindowId
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def postMaintenanceWindow(self, groupId, maintenanceWindow):
        url = self.url + 'groups/' + groupId + '/maintenanceWindows'
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, data=json.dumps(maintenanceWindow), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def patchMaintenanceWindow(self, groupId, maintenanceWindowId, payload):
        url = self.url + 'groups/' + groupId + '/maintenanceWindows/' + maintenanceWindowId
        headers = {'Content-type': 'application/json'}
        result = requests.patch(url, data=json.dumps(payload), auth=HTTPDigestAuth(self.username, self.apiKey), headers=headers)
        return json.loads(result.text)

    def delMaintenanceWindow(self, groupId, maintenanceWindowId):
        url = self.url + 'groups/' + groupId + '/maintenanceWindows/' + maintenanceWindowId
        result = requests.delete(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

# Measurements

    def getHostMeasurements(self, groupId, hostId, granularity, measurements=None, period=None, start=None, end=None):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/measurements?granularity=' + granularity
        
        if not (measurements is None):
            if (isinstance(measurements, basestring)):
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
        
        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getDiskPartitionMeasurements(self, groupId, hostId, partitionName, granularity, measurements=None, period=None, start=None, end=None):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/disks/' + partitionName +'/measurements?granularity=' + granularity
        
        if not (measurements is None):
            if (isinstance(measurements, basestring)):
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

        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)

    def getDatabaseMeasurements(self, groupId, hostId, databaseName, granularity, measurements=None, period=None, start=None, end=None):
        url = self.url + 'groups/' + groupId + '/hosts/' + hostId + '/databases/' + databaseName +'/measurements?granularity=' + granularity
        
        if not (measurements is None):
            if (isinstance(measurements, basestring)):
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

        result = requests.get(url, auth=HTTPDigestAuth(self.username, self.apiKey))
        return json.loads(result.text)





    
        

