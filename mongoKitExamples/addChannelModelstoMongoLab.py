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
        'specification': {
            'type': basestring,
            'conductance':float,
            'reversal_potential': float,
            'particles' : {
                'x_initial': float,
                'alpha':{
                    'a': float,
                    'b': float,
                    'c': float,
                    'd': float,
                    'f': float,
                    'h': float
                },
                'beta': {
                    'a': float,
                    'b': float,
                    'c': float,
                    'd': float,
                    'f': float,
                    'h': float
                },
                'power': float
        }   

    }
    }

connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)
connection.register([ModelInfo])



for x in range(0, 12):
    item1 = connection.ModelInfo({
                                 "entity_type": "channel",
                                 "entity_name": "hh_channel_vgi_1",
                                 "description": "This is an extended description of the entity",
                                 "author": "Nathan Jordan",
                                 "author_email": "njordan@cse.unr.edu",
                                 "specification": {
                                 "type": "hh_voltage_gated_ion",
                                 "conductance": 65.0,
                                 "reversal_potential": 65.0,
                                 "particles": {
                                 "x_initial": 5.0,
                                 "alpha": {
                                 "a": 0.5,
                                 "b": 0.01,
                                 "c": 1.0,
                                 "d": 50.0,
                                 "f": -10.0,
                                 "h": -1.0
                                 },
                                 "beta": {
                                 "a": 0.125,
                                 "b": 0.0,
                                 "c": 0.0,
                                 "d": 60.0,
                                 "f": 80.0,
                                 "h": 1.0
                                 },
                                 "power": 4.0
                                 }
                                 }
                                 })
    item1['entity_name'] = "hh_channel_vgi_" + str(x)
    if x % 3 == 0:
        item1['author'] = "Katie Gilgen"
    elif x % 2 == 0:
        item1['author'] = "Lander Burns"
    else:
        item1['author'] = "Aidan Dolan"
    item1.save()


