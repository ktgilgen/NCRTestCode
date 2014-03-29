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
        'votes':int,
        'specification': {
            'type': basestring,
            'm_initial': float,
            'reversal_potential': float,
            'm_power': float,
            'conductance': float,
            'forward_scale': float,
            'forward_exponent': float,
            'backwards_rate': float,
            'tau_scale': float
        }
    }

connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)
connection.register([ModelInfo])




for x in range(0, 12):
    item1 = connection.ModelInfo(
                                 {
                                 "entity_type": "channel",
                                 "entity_name": "lif_channel_calcium_dependant_1",
                                 "description": "This is an extended description of the entity",
                                 "author": "Nathan Jordan",
                                 "author_email": "njordan@cse.unr.edu",
                                 "votes": 0,
                                 "specification": {
                                 "type": "lif_calcium_dependant",
                                 "m_initial": 65.0,
                                 "reversal_potential": 65.0,
                                 "m_power": 65.0,
                                 "conductance": 65.0,
                                 "forward_scale": 65.0,
                                 "forward_exponent": 65.0,
                                 "backwards_rate": 65.0,
                                 "tau_scale": 65.0
                                 }
                                 })
    item1['entity_name'] = "lif_channel_calcium_dependant_" + str(x)
    if x % 3 == 0:
        item1['author'] = "Katie Gilgen"
    elif x % 2 == 0:
        item1['author'] = "Lander Burns"
    else:
        item1['author'] = "Aidan Dolan"
    item1.save()