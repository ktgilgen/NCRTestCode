import pymongo
from mongokit import *
import datetime
import json

class StimulusModel(Document):
    __collection__ = 'Stimulus'
    __database__ = 'brainlab_test'
    structure = {
        '_id':basestring,
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'specification': {
            'type': basestring,
            'parameters': {
                'amplitude': int,
                'width' : int,
                'frequency' : int
            },
            
            'probability' : float,
            'time_start':int,
            'time_end' : int
        
        }   
}


class Synapse_Flat(Document):
    __collection__ = 'Synapse'
    __database__ = 'brainlab_test'
    structure = {
        '_id':basestring,
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'specification': {
            'type': basestring,
            'parameters': {
                'delay': float,
                'current' : float
        }
        
        }   
}

class Synapse_NCS(Document):
    __collection__ = 'Synapse'
    __database__ = 'brainlab_test'
    structure = {
        '_id':basestring,
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'specification': {
            'type': basestring,
            'parameters': {
                'utilization': float,
                'redistribution' : float,
                'last_prefire_time' : float,
                'last_postfire_time' :  float,
                'tau_facilitation' : float,
                'tau_depression' : float,
                'tau_ltp' : float,
                'tau_ltd' : float,
                'a_ltp_minimum' : float,
                'a_ltd_minimum' : float,
                'max_conductance' : float,
                'reversal_potential': float,
                'tau_postsynaptic_conductance' : float,
                'psg_waveform_duration' : float,
                'delay' : float
        }
        
        }   
}


connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)

connection.register([StimulusModel, Synapse_Flat, Synapse_NCS])
stimItem = connection.StimulusModel({
                               "_id": "df90sahf0sd9ha8sdhf8dhsa",
                               "entity_type": "stimulus",
                               "entity_name": "stimulus_1",
                               "description": "This is an extended description of the entity",
                               "author": "Nathan Jordan",
                               "author_email": "njordan@cse.unr.edu",
                               "specification":{
                               "type": "rectangular_current",
                               "parameters": {
                               "amplitude": 2,
                               "width": 3,
                               "frequency": 10
                               },
                               "probability": 0.5,
                               "time_start": 612789,
                               "time_end": 1378454
                               }
                               })

synapseItem = connection.Synapse_Flat({
                                      "_id": "hfasdhf8shfasdhf8h8hasd8f",
                                      "entity_type": "synapse",
                                      "entity_name": "synapse_2",
                                      "description": "This is an extended description of the entity",
                                      "author": "Nathan Jordan",
                                      "author_email": "njordan@cse.unr.edu",
                                      "specification": {
                                      "type": "flat",
                                      "parameters": {
                                      "delay": 65.0,
                                      "current": 65.0
                                      }
                                      }
                                      })

ncsSynapseItem = connection.Synapse_NCS({
                                        "_id": "hfasdhf8shfasdhf8h8hasd8f",
                                        "entity_type": "synapse",
                                        "entity_name": "synapse_1",
                                        "description": "This is an extended description of the entity",
                                        "author": "Nathan Jordan",
                                        "author_email": "njordan@cse.unr.edu",
                                        "specification": {
                                        "type": "ncs",
                                        "parameters":{
                                        "utilization": 65.0,
                                        "redistribution": 65.0,
                                        "last_prefire_time": 65.0,
                                        "last_postfire_time": 65.0,
                                        "tau_facilitation": 65.0,
                                        "tau_depression": 65.0,
                                        "tau_ltp": 65.0,
                                        "tau_ltd": 65.0,
                                        "a_ltp_minimum": 65.0,
                                        "a_ltd_minimum": 65.0,
                                        "max_conductance": 65.0,
                                        "reversal_potential": 65.0,
                                        "tau_postsynaptic_conductance": 65.0,
                                        "psg_waveform_duration": 65.0,
                                        "delay": 65.0
                                        }
                                        }
                                        })

for x in range(0, 10):
    stimItem['_id'] = 'stim' + str(x)
    synapseItem['_id'] = 'synapse' + str(x)
    ncsSynapseItem['_id'] = 'synapse_ncs' + str(x)
    
    stimItem.save()
    synapseItem.save()
    ncsSynapseItem.save()