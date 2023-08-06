import json
import questionary

from .idp_utils import *

class GroupManager:
    def __init__(self, credentials, url, env):
        print ("\nEntered group manager with credentials: \n{} \nand url: \n\t{} \n".format(json.dumps(credentials, indent=3), url))
        self.environment = env

        self.httpsIdpHost = "https://" + url
        self.accessTokenURL =    self.httpsIdpHost + "/auth/realms/master/protocol/openid-connect/token"
        self.getAllGroupsURL =   self.httpsIdpHost + "/auth/admin/realms/pricesmart/groups"
        self.getGroupInfoURL =   self.httpsIdpHost + "/auth/admin/realms/pricesmart/groups/{}"
        self.addUserToGroupURL = self.httpsIdpHost + "/auth/admin/realms/pricesmart/users/{}/groups/{}"
        self.getAllUsersURL =    self.httpsIdpHost + "/auth/admin/realms/pricesmart/users"

        self.accessToken = None

        self.credentials = credentials
        self.managerOptions = {
            "Create a group": self.createGroup,
            "Add Roles to group": self.addRolesParams
        }

    ################################################### PUBLIC METHODS ###################################################

    def main(self):
        actionDict = selectOption("Select an action to perform:", self.managerOptions)
        selectedActionName = actionDict['key']
        selectedActionImp = actionDict['value']
        
        #Execute the function inside the selected option
        params = selectedActionImp()

        result = {
            "action": selectedActionName,
            "params": params,
            "description": params["description"]
        }
        return result

    def createGroup(self, **kwargs):
        print ("Creating group")
        
    def addRolesParams(self, **kwargs):
        selectedGroup = self.selectGroupFromIDP()
        groupId = selectedGroup["id"]

        rolesToAdd = []

        loadFile = questionary.confirm("Do you have a roles file to enter?").ask()
        if loadFile:
            questionary.text("Enter path to roles file")
            # TODO: retrieve all roles from file path
        else: 
            cont = True
            while cont:
                nextRole = questionary.text("Type role (press enter to continue)").ask()
                if nextRole == "": 
                    cont = False
                else: 
                    rolesToAdd.append(nextRole)
        
        correct = questionary.confirm("\nAdding roles: {} \nto group: {} \nin environment: {}\nIs this correct?"
            .format(rolesToAdd, selectedGroup["name"], self.environment)).ask()

        if(correct):
            return {"roles": rolesToAdd,
                    "groupId": selectedGroup["id"],
                    "groupName": selectedGroup["name"],
                    "description": "Add: {} roles to group: {}".format(rolesToAdd, selectedGroup["name"])}

    ################################################### PRIVATE METHODS ###################################################

    def selectGroupFromIDP(self):
        self.accessToken = getAccessToken(self.accessTokenURL, self.credentials, self.accessToken)
        allIDPGroups = protectedRequest("GET", self.getAllGroupsURL, self.accessToken['access_token'])
        groupHash = {}
        for group in allIDPGroups:
            groupHash[group["name"]] = group
        selectedGroup = selectOption("Which of these available groups do you want to add roles to?", groupHash)["value"]
        return selectedGroup
        
             
    def actions(self, action=0):
        if option <= 0:
            return managerOptions
        else: 
            return managerOptions[action]
