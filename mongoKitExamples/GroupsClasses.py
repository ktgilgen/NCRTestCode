import pymongo
from mongokit import *
import datetime
import json

class Group(Document):
    __collection__ = 'Neuron_Group'
    __database__ = 'brainlab_test'
    structure = {
        '_id':basestring,
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'geometry': {'width': int, 'height': int, 'depth': int},
        'subgroups':  [{'model_id': basestring, 'label': basestring, 
                        'location': {'x': int, 'y': int, 'z': int}
                        }] ,
        'neuron_groups': [{ 'neuron': basestring, 'label': basestring,   
                            'geometry': { 'width': int, 'height': int, 'depth': int},
                            'location': { 'x': int, 'y': int, 'z': int}
                        }],
        'aliases': { 'model_aliases': [ {  'alias': basestring, 'labels': [basestring]}],
                     'synaptic_aliases': [ {'alias': basestring, 'labels': [basestring]} ]
        },
        'connections': [{ 'presynaptic': basestring, 'postsynaptic': basestring,
                        'probability': float, 'synapse': basestring, 'recurrent': basestring}]
        
    }
    required_fields=['_id']
    default_values={}