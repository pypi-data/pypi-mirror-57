import requests
import json
import questionary
import os

import time

environmentURLs = {
    "DEV": "identity-provider-psmt-dev.aeropost.com",
    "STAGE": "identity-provider-psmt-stage.aeropost.com",
    "PROD": "identity-provider-psmt.aeropost.com"
}


def selectOption(message, options):
    """Prompts the user to select an option and returns 
    the value of the selected key

    Arguments:
        message {string} -- The message that will be displayed to the user 
        options {dict} -- a dictionary where the key should be a string that will 
        be shown to the user as an option and the value should be what will be 
        returned if the key is selected 

    Returns:
        dict -- a dictionary where 'key' will be the selected option and 
        'value' will be the value of the selected option
    """
    option = questionary.select(message,
                                choices=list(options.keys())).ask()

    return {'key': option,
            'value': options[option]}


def getAdminHeaders(accessToken):
    """Returns headers necessary for sending an access token to the 
    IDP is intended for internal use only

    Arguments:
        accessToken {object} -- an object describing the headers necessary for the IDP

    Returns:
        object -- an object describing the headers necessary for the IDP
    """
    adminHeaders = {
        'Authorization': "Bearer {}".format(accessToken),
        'Connection': "Keep-Alive",
        'Accept': "application/json",
        'Cache-Control': "no-cache",
        'accept-encoding': "gzip, deflate",
        'cache-control': "no-cache"
    }
    return adminHeaders


def checkTokenExpiry(accessTokenObject):
    """Checks to see if your access token is still valid
    WARNGING: this method relies on you getting your access token 
    from getAccessToken in this same module

    Arguments:
        accessTokenObject {object} -- the access token that is being checked

    Returns:
        boolean -- True is still valid, False if no longer valid
    """

    if accessTokenObject["valid_until"] is None:
        # we cannot determine if the token is still valid or not so just return false.
        # Probably means the token was retrieved from a different source than
        # getAccessToken() of this same module
        return False
    if(time.time() > accessTokenObject["valid_until"]):
        print ("Current token has expired")
        return False
    return True


def getAccessToken(requestURL, credentials, accessToken=None):
    """This function retrieves an access token from the idp to be used 
    in other adminstrative requests

    Arguments:
        requestURL {stirng} -- url from where the access token should be retreived from
        credentials {dict} -- object describing the credentials of the user/client to be used
        accessToken {dict} -- (optional) a previously requested access token. If included this method 
                              will check if it is currently valid and either return the same token or 
                              get a new one. 

    Returns:
        dict -- the returned response plus an extra 'expires_in' field
    """
    if accessToken is not None:
        if checkTokenExpiry(accessToken):
            return accessToken

    print ("Getting new access token")
    accessTokenRequest = requests.post(
        requestURL, data=credentials, verify=False)
    jsonAccessTokenResponse = json.loads(accessTokenRequest.text)
    print ("Got the following access token: \n{} \n\n".format(
        json.dumps(jsonAccessTokenResponse, indent=3)))
    expiresIn = jsonAccessTokenResponse["expires_in"]
    jsonAccessTokenResponse["valid_until"] = time.time() + expiresIn
    return jsonAccessTokenResponse


def protectedRequest(method, url, accessToken, body=None):
    """Executes a request protected by and access token in the IDP 

    Arguments:
        url {string} -- the url to where the request should be executed
        accessToken {string} -- an access token valid for the IDP
        method {string} -- describes the type of request that will be made
        body {object} -- optional body to be sent in the request

    Returns:
        any -- The response object of the resource called
    """
    print ("Making access token protected {} request to: {}".format(method, url))
    protectedRequest = requests.request(
        method, url, headers=getAdminHeaders(accessToken), verify=False, json=body)

    if protectedRequest.status_code == 200 or protectedRequest.status_code == 201\
    or protectedRequest.status_code == 204:
        try:
            response = json.loads(protectedRequest.text)
        except:
            response = ''
        
        print ("Got the following response:")
        print (json.dumps(response, indent=3))
        return response
    else:
        raise Exception("Could not execute request to '{}' received status code '{}'".format(
            url, protectedRequest.status_code))


def optionsToString(options):
    optionsString = ""
    for key, value in options.iteritems():
        optionsString += "\n\t{}. {}".format(str(key), str(value["desc"]))
    return optionsString


def buildCredentials(envQuestion, envExceptions=[]):
    """asks for an environment and either retreives credentials from the corresponding 
    credentials file or asks user for credentials
    
    Arguments:
        envQuestion {string} -- question to ask while asking for environment
    
    Keyword Arguments:
        envExceptions {string} -- [environments not to include as options in environments] (default: {[]})
        
    Returns:
        [object] -- [an object containing credentials for the environment, the environment and the base url]
    """
    choices = list(environmentURLs.keys())
    for exception in envExceptions: 
        choices.remove(exception)
    
    envQuestion = questionary.select(envQuestion, choices)
    env = envQuestion.ask()
    baseUrl = environmentURLs[env]
    try:
        with open(os.getenv("HOME") + "/.kcman/" + env + "-credentials.json") as credFile:
            useFile = questionary.confirm("Found credentials file for {} environment, use these credentials? y/n ".format(env))
            if useFile.ask():
                idpCredentials = json.load(credFile)
            else:
                raise Exception ("Declined to use credentials file for {} environment".format(env))
    except Exception as exception:
        print ("Please enter valid credentials for {} environment IDP".format(env))
        username = questionary.text("username:").ask()
        password = questionary.text("password:").ask()
        client_id = questionary.text("client id:").ask()
        client_secret = questionary.text("client secret:").ask()

        idpCredentials = {
            "grant_type": "password",
            "username": username,
            "password": password,
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": "openid email profile"
        }
    
    return {
        "env": env,
        "baseUrl": baseUrl,
        "credentials": idpCredentials
    }
