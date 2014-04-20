import pymongo
from mongokit import *
import datetime
import json

class ModelInfo(Document):
    __collection__ = 'Channels'
    __database__ = 'brainlab_test'
    structure = {
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'author_id' : basestring,
        'scope' : basestring,
        'votes' : int,
        'specification': {
            'type': basestring,
            'v_half': float,
            'r': float,
            'activation_slope': float,
            'deactivation_slope': float,
            'equilibrium_slope': float,
            'conductance': float,
            'reversal_potential': float,
            'm_initial': float,
            'm_power': float
                
            }
    }

connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)
connection.register([ModelInfo])

for x in range(0, 4):
    item1 = connection.ModelInfo(
                                 {
                                 "entity_type": "channel",
                                 "entity_name": "lif_channel_vgi_1",
                                 "description": "This is an extended description of the entity",
                                 "author": "Alex Falconi",
                                 "author_email": "exavior75@yahoo.com",
                                 "votes": 0,
                                 "scope" : "UNR",
                                 "author_id" : "5346e8b51d41c810b40ccc3c",
                                 "specification": {
                                 "type": "lif_voltage_gated_ion",
                                 "v_half": 65.0,
                                 "r": 65.0,
                                 "activation_slope": 65.0,
                                 "deactivation_slope": 65.0,
                                 "equilibrium_slope": 65.0,
                                 "conductance": 65.0,
                                 "reversal_potential": 65.0,
                                 "m_initial": 65.0,
                                 "m_power": 65.0
                                 }
                                 })
    item1['entity_name'] = "lif_channel_vgi_" + str(x)
    if x % 3 == 0:
        item1['author'] = "Katie Gilgen"
        item1['author_email'] = "ktgilgen@gmail.com"
        item1['author_id'] = "53543c681d41c80bc6a98b07"
        item1['scope'] = "UNR"
    
    
    elif x % 2 == 0:
        item1['author'] = "Big Farma"
        item1['author_email'] = "bigfarma@gmail.com"
        item1['author_id'] = "53543c8d1d41c80bc6a98b08"
        item1['scope'] = "Cincinnati Neuroscience"
    item1.save()




