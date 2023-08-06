import json
import questionary


from .group_manager import GroupManager
from .clients_manager import ClientManager
from .migration_manager import PersistanceItem
from .user_manager import UserManager

from .credentials_manager import CredentialsManager

from .idp_utils import *


environmentURLs = {
    "DEV": "identity-provider-psmt-dev.aeropost.com",
    "STAGE": "identity-provider-psmt-stage.aeropost.com",
    "PROD": "identity-provider-psmt.aeropost.com" 
}

availableManagers = {
    "Role manager": None,
    "Group manager": GroupManager,
    "Clients manager": ClientManager,
    "User manager": UserManager
}

def main(**kwargs):
    if '-c' in kwargs or '--credentials' in kwargs:
        credentialsManager = CredentialsManager()
        credentialsManager.main()

    if '-m' in kwargs or '--manager' in kwargs or kwargs == {}:
        environmentInfo = buildCredentials("Are you using?")
        environment = environmentInfo["env"]
        requestURL = environmentInfo["baseUrl"]
        idpCredentials = environmentInfo["credentials"]

        manager = selectOption("Which manager do you need to use?", availableManagers)
        managerName = manager["key"]
        managerModule = manager["value"]
        
        managerModule = managerModule(idpCredentials, requestURL, environment)
        results = managerModule.main()