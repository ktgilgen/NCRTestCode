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



for x in range(0, 7):
    item1 = connection.ModelInfo({
                                 "entity_type": "channel",
                                 "entity_name": "hh_channel_vgi_1",
                                 "description": "This is an extended description of the entity",
                                 "author": "Alex Falconi",
                                 "author_email": "exavior75@yahoo.com",
                                 "author_id" : "5346e8b51d41c810b40ccc3c",
                                 "votes" : 0,
                                 "scope" : "UNR",
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
        item1['author_email'] = "ktgilgen@gmail.com"
        item1['author_id'] = "53543c681d41c80bc6a98b07"
        item1['scope'] = "UNR"
    
    
    elif x % 2 == 0:
        item1['author'] = "Big Farma"
        item1['author_email'] = "bigfarma@gmail.com"
        item1['author_id'] = "53543c8d1d41c80bc6a98b08"
        item1['scope'] = "Cincinnati Neuroscience"
    item1.save()


