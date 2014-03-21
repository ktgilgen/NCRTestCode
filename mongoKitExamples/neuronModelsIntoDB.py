import pymongo
from mongokit import *
import datetime
import json

class HHNeuron(Document):
    __collection__ = 'Neuron'
    __database__ = 'brainlab_test'
    structure = {
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'specification': {
            'type': basestring,
            'threshold' : float,
            'resting_potential' : {'type':basestring, 'min' :float, 'max' : float},
            
            'capacitance' : float,
            'channels':[basestring]
            ,
        }   
    }


class IZHNeuron(Document):
    __collection__ = 'Neuron'
    __database__ = 'brainlab_test'
    structure = {
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'specification': {
            'type': basestring,
                'a': float,
                'b' : float,
                'c' : float,
                'd' : float,
                'u' : float,
                'v' : float,
                'threshold': int
        }   
    }

class NCSNeuron(Document):
    __collection__ = 'Neuron'
    __database__ = 'brainlab_test'
    structure = {
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'specification': {
            'type': basestring,
                'spikeshape': [int],
                'threshold': float,
                'resting_potential' : { 'type' : basestring, 'min' : float, 'max' : float },
                'calcium' : {'type': basestring, 'mean' : float, 'standard_deviation' : float},
                'calcium_spike_increment' : float,
                'tau_calcium' : float,
                'leak_reversal_potential' : float,
                'leak_conductance' : float,
                'tau_membrane' : float,
                'r_membrane' : float,
                'channels' : [basestring]
            
        
        }   
}

connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)

connection.register([HHNeuron, IZHNeuron, NCSNeuron])


for x in range(0, 10):
    ncsItem = connection.NCSNeuron({
                                   "entity_type": "neuron",
                                   "entity_name": "ncs_neuron_1",
                                   "description": "This is an extended description of the entity",
                                   "author": "Nathan Jordan",
                                   "author_email": "njordan@cse.unr.edu",
                                   "specification": {
                                   "type": "ncs",
                                   "spikeshape": [
                                                  -12,
                                                  0,
                                                  5,
                                                  60,
                                                  70,
                                                  20,
                                                  23
                                                  ],
                                   "threshhold": 65.0,
                                   "resting_potential": {
                                   "type": "uniform",
                                   "min": -23.0,
                                   "max": -30.0
                                   },
                                   "calcium": {
                                   "type": "normal",
                                   "mean": 6.0,
                                   "standard_deviation": 0.5
                                   },
                                   "calcium_spike_increment": 65.0,
                                   "tau_calcium": 65.0,
                                   "leak_reversal_potential": 65.0,
                                   "leak_conductance": 65.0,
                                   "tau_membrane": 65.0,
                                   "r_membrane": 65.0,
                                   "channels": [
                                                "hf8dshf8asdh80fdsh80fadsh80f",
                                                "nfhasf90dsh90fhads90fhassd9a"
                                                ]
                                   }
                                   })

    hhItem = connection.HHNeuron({
                             "entity_type": "neuron",
                             "entity_name": "hh_neuron_1",
                             "description": "This is an extended description of the entity",
                             "author": "Nathan Jordan",
                             "author_email": "njordan@cse.unr.edu",
                             "specification": {
                             "type": "hh",
                             "threshhold": 65.0,
                             "resting_potential": {
                             "type": "uniform",
                             "min": -23.0,
                             "max": -30.0
                             },
                             "capacitance": 65.0,
                             "channels": [
                                          "hf892f82hf8023hf032h0fh3209fh2",
                                          "80fhdhahifhsifsdiofhiadsfhasja"
                                          ]
                             }
                             })

    izhItem = connection.IZHNeuron({
                               "entity_type": "neuron",
                               "entity_name": "neuron_izh_1",
                               "description": "This is an extended description of the entity",
                               "author": "Nathan Jordan",
                               "author_email": "njordan@cse.unr.edu",
                               "specification": {
                               "type": "izhikevich",
                               "a": 0.02,
                               "b": 0.2,
                               "c": -65.0,
                               "d": 8.0,
                               "u": -12.0,
                               "v": -65.0,
                               "threshold": 30
                               }
                               })
    if x %  3 == 0:
        ncsItem['author'] = "Riley Carroll"
        hhItem['author'] = "Lander Burns"
        izhItem['author'] = "Aidan Dolan"
    
    ncsItem['entity_name'] = 'ncs' + str(x)
    hhItem['entity_name'] = 'hh' + str(x)
    izhItem['entity_name'] = 'izh' + str(x)
    
    ncsItem.save()
    hhItem.save()
    izhItem.save()
