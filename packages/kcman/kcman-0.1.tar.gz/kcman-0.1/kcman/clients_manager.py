import json
import questionary

from .idp_utils import *


class ClientManager: 
    def __init__(self, credentials, url, env):
        print ("\nEntered clients manager with credentials: \n{} \nand url: \n\t{} \n".format(json.dumps(credentials, indent=3), url))
        self.environment = env

        self.httpsIdpHost = "https://" + url
        self.accessTokenURL =          self.httpsIdpHost + "/auth/realms/master/protocol/openid-connect/token"
        self.baseClientsURL =          self.httpsIdpHost + "/auth/admin/realms/pricesmart/clients"
        self.clientServiceAccountURL = self.httpsIdpHost + "/auth/admin/realms/pricesmart/clients/{}/service-account-user"
        self.serviceAccountRoles =     self.httpsIdpHost + "/auth/admin/realms/pricesmart/users/{}/role-mappings/realm"
        self.getClientSecret =         self.httpsIdpHost + "/auth/admin/realms/pricesmart/clients/{}/client-secret"

        self.accessToken = None

        self.credentials = credentials
        self.managerOptions = {
            "Create a client": self.createClient,
            "Copy client": self.copyClient
        }


################################################### PUBLIC METHODS ###################################################

    def main(self):
        actionDict = selectOption("Select an action to perform:", self.managerOptions)
        selectedActionName = actionDict['key']
        selectedActionImp = actionDict['value']

        params = selectedActionImp()

################################################### PRIVATE METHODS ###################################################            

    def createClient(self, client):
        self.accessToken = getAccessToken(self.accessTokenURL, self.credentials, self.accessToken)
        protectedRequest("POST", self.baseClientsURL, self.accessToken['access_token'], client)

    def extractDictValue(self, roles, value):
        roleNames = []
        for role in roles: 
            roleNames.append(role[value])
        return roleNames

    def copyClient(self):
        environmentInfo = buildCredentials("Copy to:", [self.environment])
        environment = environmentInfo["env"]
        requestURL = environmentInfo["baseUrl"]
        idpCredentials = environmentInfo["credentials"]

        self.accessToken = getAccessToken(self.accessTokenURL, self.credentials, self.accessToken)
        clients = protectedRequest("GET", self.baseClientsURL, self.accessToken['access_token'])
        clientIds = []
        for client in clients:
            clientIds.append(client['clientId'])
        selectedClientId = questionary.select('Select a client to copy:', choices=clientIds).ask()

        selectedClientIdIndex = clientIds.index(selectedClientId)
        selectedClient = clients[selectedClientIdIndex]
        
        # retreive client service account 
        clientServiceAccount = protectedRequest("GET", self.clientServiceAccountURL.format(selectedClient['id']), self.accessToken['access_token'])

        # retreive client service account roles
        clientServiceAccountRoles = protectedRequest("GET", self.serviceAccountRoles.format(clientServiceAccount['id']), self.accessToken['access_token'])
        clientServiceAccountRoleNames = self.extractDictValue(clientServiceAccountRoles, 'name')

        print('roles to add: \n{}'.format(clientServiceAccountRoles))

        # get all realm roles in target environment
        targetEnvAccessToken = getAccessToken('https://' + requestURL + '/auth/realms/master/protocol/openid-connect/token', idpCredentials)
        targetEnvRealmRoles = protectedRequest("GET", 'https://' + requestURL + '/auth/admin/realms/pricesmart/roles', targetEnvAccessToken['access_token'])
        targetEnvRealmRoleNames = self.extractDictValue(targetEnvRealmRoles, 'name')
        
        # compare service account roles with target env roles
        missingRoles = []
        for role in clientServiceAccountRoleNames:
            if role not in targetEnvRealmRoleNames:
                missingRoles.append(role)
        
        if len(missingRoles) != 0:
            print("{} environment is missing the following roles to be able to copy {} client".format(environment, missingRoles, selectedClientId))
        
        # create the client 
        targetEnvAccessToken = getAccessToken('https://' + requestURL + '/auth/realms/master/protocol/openid-connect/token', idpCredentials, targetEnvAccessToken)
        protectedRequest("POST", 'https://' + requestURL + '/auth/admin/realms/pricesmart/clients', targetEnvAccessToken['access_token'], selectedClient)

        # retreive new client service account 
        targetEnvAccessToken = getAccessToken('https://' + requestURL + '/auth/realms/master/protocol/openid-connect/token', idpCredentials, targetEnvAccessToken)
        targetEnvAllClients = protectedRequest("GET", 'https://' + requestURL + '/auth/admin/realms/pricesmart/clients', targetEnvAccessToken['access_token'])

        for client in targetEnvAllClients: 
            if (client['clientId'] == selectedClient['clientId']):
                targetClientId = client['id']
                break

        targetServiceAccount = protectedRequest("GET", 'https://' +  requestURL + '/auth/admin/realms/pricesmart/clients/{}/service-account-user'.format(targetClientId), targetEnvAccessToken['access_token'])
        targetServiceAccountId = targetServiceAccount['id']

        # add necessary roles to the new service account
        newRoleList = []
        for role in clientServiceAccountRoleNames:
            # get role to add's id
            for targetEnvRole in targetEnvRealmRoles:
                if targetEnvRole['name'] == role:
                    newRole = {}
                    newRole['name'] = role
                    newRole['id'] = targetEnvRole['id']
                    newRoleList.append(newRole)
                    break
        protectedRequest("POST", 'https://' +  requestURL + '/auth/admin/realms/pricesmart/users/{}/role-mappings/realm'.format(targetServiceAccountId), targetEnvAccessToken['access_token'], newRoleList)

        # set new client service account roles 
        print('created a new client in {}'.format(environment))
