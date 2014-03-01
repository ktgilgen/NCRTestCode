import pymongo
from mongokit import *
import datetime
import json

class ModelInfo(Document):
    __collection__ = 'Channels'
    __database__ = 'brainlab_test'
    structure = {
        '_id':basestring,
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'channel_parameters': {
            'type': basestring,
            'm_initial': {
                'type':basestring,
                'value': float
            },
            'reversal_potential': {
                'type':basestring,
                'value': float
            },
            'm_power': {
                'type':basestring,
                'value': float
            },
            'conductance': {
                'type':basestring,
                'value': float
            },
            'forward_scale': {
                'type':basestring,
                'value': float
            },
            'forward_exponent': {
                'type':basestring,
                'value': float
            },
            'backwards_rate': {
                'type':basestring,
                'value': float
            },
            'tau_scale': {
                'type':basestring,
                'value': float
        }
    }
    }
    required_fields=['_id']
    default_values={}
connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)
connection.register([ModelInfo])


#standard find with filtered return values
for doc in connection.brainlab_test.Channels.find({"author": "Lander Burns"}, {"author": 1}):
    print doc

#fetching find only those matching structure 
#for doc in connection.ModelInfo.fetch({"entity_type":"channel"}, {"entity_name": 1} ):
#    print doc

#finds a random document
print connection.ModelInfo.find_random()


