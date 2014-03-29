import pymongo
from mongokit import *
import datetime
import json

class StimulusModel(Document):
    __collection__ = 'Stimulus'
    __database__ = 'brainlab_test'
    structure = {
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'votes' : int,
        'specification': {
            'type': basestring,
            'amplitude': int,
            'width' : int,
            'frequency' : int,            
            'probability' : float,
            'time_start':int,
            'time_end' : int
        
        }   
}


class Synapse_Flat(Document):
    __collection__ = 'Synapse'
    __database__ = 'brainlab_test'
    structure = {
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'votes' : int, 
        'specification': {
            'type': basestring,
                'delay': float,
                'current' : float  
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
        'votes' : int,
        'specification': {
            'type': basestring,
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


connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)

connection.register([StimulusModel, Synapse_Flat, Synapse_NCS])


for x in range(0, 10):
    stimItem = connection.StimulusModel({
                                        "entity_type": "stimulus",
                                        "entity_name": "stimulus_1",
                                        "description": "This is an extended description of the entity",
                                        "author": "Nathan Jordan",
                                        "author_email": "njordan@cse.unr.edu",
                                        "votes" : 0,
                                        "specification":{
                                        "type": "rectangular_current",
                                        "amplitude": 2,
                                        "width": 3,
                                        "frequency": 10,
                                        "probability": 0.5,
                                        "time_start": 612789,
                                        "time_end": 1378454
                                        }
                                        })

    synapseItem = connection.Synapse_Flat({
                                      "entity_type": "synapse",
                                      "entity_name": "synapse_2",
                                      "description": "This is an extended description of the entity",
                                      "author": "Nathan Jordan",
                                      "author_email": "njordan@cse.unr.edu",
                                          "votes" : 0,
                                      "specification": {
                                      "type": "flat",
                                      "delay": 65.0,
                                      "current": 65.0
                                      }
                                      })

    ncsSynapseItem = connection.Synapse_NCS({
                                        "entity_type": "synapse",
                                        "entity_name": "synapse_1",
                                        "description": "This is an extended description of the entity",
                                        "author": "Nathan Jordan",
                                        "author_email": "njordan@cse.unr.edu",
                                            "votes" : 0,
                                        "specification": {
                                        "type": "ncs",
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
                                        })
    if x % 2 == 0:
        stimItem['author'] = "Alex Falconi"
        ncsSynapseItem['author'] = "Alex Falconi"
        synapseItem['author'] = "Alex Falconi"
    stimItem['entity_name'] = 'stim' + str(x)
    synapseItem['entity_name'] = 'synapse' + str(x)
    ncsSynapseItem['entity_name'] = 'synapse_ncs' + str(x)
    
    stimItem.save()
    synapseItem.save()
    ncsSynapseItem.save()