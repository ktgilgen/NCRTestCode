import pymongo
from mongokit import *
import datetime
import json

class HHNeuron(Document):
    __collection__ = 'Neuron'
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
                'threshold': int,
                    'resting_potential' : {'type':basestring, 'min' :float, 'max' : float},
            
            'capacitance' : float,
            'channels':[basestring]
            },
        }   
    }


class IZHNeuron(Document):
    __collection__ = 'Neuron'
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
                'a': float,
                'b' : float,
                'c' : float,
                'd' : float,
                'u' : float,
                'v' : float,
                'threshold': int
            }
        
        }   
    }

class NCSNeuron(Document):
    __collection__ = 'Neuron'
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
                'spikeshape': [int],
                'threshold': int,
                'resting_potential' : { 'type' : basestring, 'mean' : float, 'standard_deviation' : float },
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
}

connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)

connection.register([HHNeuron, IZHNeuron, NCSNeuron])
ncsItem = connection.NCSNeuron({
                                                  "_id": "df90sahf0sd9ha8sdhf8dhsa",
                                                  "entity_type": "neuron",
                                                  "entity_name": "BasalGanglia",
                                                  "description": "This is an extended description of the entity",
                                                  "author": "Nathan Jordan",
                                                  "author_email": "njordan@cse.unr.edu",
                                                  "specification": {
                                                  "type": "ncs",
                                                  "parameters": {
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
                                                  }
                                                  })

hhItem = connection.HHNeuron({
                             "_id": "df90sahf0sd9ha8sdhf8dhsa",
                             "entity_type": "neuron",
                             "entity_name": "BasalGanglia",
                             "description": "This is an extended description of the entity",
                             "author": "Katie Gilgen",
                             "author_email": "ktgilgen@gmail.com",
                             "specification": {
                                "type": "hh",
                                "parameters": {
                                    "threshhold": 65.0,
                                    "resting_potential": {"type": "uniform","min": -23.0,"max": -30.0},
                                    "capacitance": 65.0,
                                    "channels": [
                                          "hf892f82hf8023hf032h0fh3209fh2",
                                          "80fhdhahifhsifsdiofhiadsfhasja"
                                          ]
                                }
                             }
                             })
izhItem = connection.IZHNeuron({
                               "_id": "ajsd9fd90ha0hsd80fhd80sha",
                               "entity_type": "neuron",
                               "entity_name": "neuron_izh_1",
                               "description": "This is an extended description of the entity",
                               "author": "Nathan Jordan",
                               "author_email": "njordan@cse.unr.edu",
                               "specification": {
                               "type": "izhikevich",
                               "parameters": {
                               "a": 0.02,
                               "b": 0.2,
                               "c": -65.0,
                               "d": 8.0,
                               "u": -12.0,
                               "v": -65.0,
                               "threshold": 30
                               }
                               }
                               })

for x in range(0, 10):
    ncsItem['_id'] = 'ncs' + str(x)
    hhItem['_id'] = 'hh' + str(x)
    izhItem['_id'] = 'izh' + str(x)
    ncsItem.save()
    hhItem.save()
    izhItem.save()
