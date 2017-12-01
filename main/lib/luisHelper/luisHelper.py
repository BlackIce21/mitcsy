
# coding: utf-8

# # Library Functions

from .luis_sdk import LUISClient
import json
from pprint import pprint

# # Helper Functions

# ### Credentials Function:

def getLUISCreds():
    credentials = json.load(open('../credentials.json'))
    luisCreds = credentials['cognitiveServices']['luis']
    return luisCreds


# ### Intent and Entities Functions:

def getPrediction(text,luisCreds):
    luisClient = LUISClient(luisCreds['appID'], luisCreds['key'], True)
    res = luisClient.predict(text)
    return res

def getIntent(res):
    return res.get_top_intent().get_name()

def getEntities(res):
    entities = []
    for entitity in res.get_entities():
        print(entitity.get_type() + " : " + entitity.get_name())
        entity = {entitity.get_type():entitity.get_name()}
        entities.append(entity)
    return entities

def getIntentAndEntities(text):
    luisCreds = getLUISCreds()
    result = getPrediction(text,luisCreds)
    pprint(result)
    intent = getIntent(result)
    pprint(intent)
    entities = getEntities(result)
    pprint(entities)
    result = {"intent" : intent,
              "entities" : entities
             }
    return result
