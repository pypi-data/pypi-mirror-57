import json 
import questionary
import os

from .idp_utils import *

class CredentialsManager:
    def __init__(self):
        self.credentialsRoute = os.getenv("HOME") + "/.kcman/"

    def main(self): 
        self.storeCredentials()

    def storeCredentials(self):
        environmentInfo = buildCredentials("Store credentials for:")
        credentialsFile= open(self.credentialsRoute + environmentInfo['env'] + '-credentials.json',"w+")
        credentialsFile.write(str(environmentInfo['credentials']))