import json
import questionary

from .idp_utils import *

class UserManager: 
    def __init__(self, credentials, url, env):
        self.httpsIdpHost = "https://" + url
        self.accessTokenURL =          self.httpsIdpHost + "/auth/realms/master/protocol/openid-connect/token"
        self.getUsersURL =          self.httpsIdpHost + "/auth/admin/realms/pricesmart/users?max=6000&briefRepresentation=true"

        self.accessToken = None
        self.credentials = credentials

        self.managerOptions = {
            "Search User List": self.searchUsers
        }

    def main(self):
        actionDict = selectOption("Select an action to perform:", self.managerOptions)
        selectedActionName = actionDict['key']
        selectedActionImp = actionDict['value']

        params = selectedActionImp()

    def searchUsers(self): 
        self.accessToken = getAccessToken(self.accessTokenURL, self.credentials, self.accessToken)
        allUsers = protectedRequest("GET", self.getUsersURL, self.accessToken['access_token'])
        as400Users = []

        for user in allUsers: 
            if not "@" in user['username'] and not user['username'].isdigit():
                try:
                    as400Users.append(user['username'])
                except:
                    pass
                
        print(as400Users)