from NeuronClasses.py import *
import pymongo
from mongokit import *
import datetime
import json

connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)
connection.register([HodgkinHuxley, NCS, Izhikevich])

ncsNeuron = connection.NCS({ "_id": "df90sahf0sd9ha8sdhf8dhsa",
                                     "entity_type": "neuron",
                                     "entity_name": "BasalGanglia",
                                     "description": "This is an extended description of the entity",
                                     "author": "Nathan Jordan",
                                     "author_email": "njordan@cse.unr.edu",
                             "specification": {
                             "type": "ncs",
                             "parameters": {
                                     "spikeshape": [-12,0,5,60,70,20,23],
                                     "threshhold": {"type": "exact","value": 65.0},
                                     "resting_potential": {"type": "uniform","min": -23.0,"max": -30.0},
                                     "calcium": {"type": "normal","mean": 6.0,"standard_deviation": 0.5},
                                     "calcium_spike_increment": {"type": "exact","value": 65.0},
                                     "tau_calcium": {"type": "exact","value": 65.0},
                                     "leak_reversal_potential": {"type": "exact","value": 65.0},
                                     "leak_conductance": {"type": "exact","value": 65.0},
                                     "tau_membrane": {"type": "exact","value": 65.0},
                                     "r_membrane": {"type": "exact","value": 65.0},
                                     "channels": [
                                                  {"channel_id": "kfjdasfj90j90ahs90dhf", "count": 4},
                                                  {"channel_id": "jf890dash8sdghf89asghdf","count": 4}]
                                     }}})
hhNeuron = connection.HodgkinHuxley({"_id": "df90sahf0sd9ha8sdhf8dhsa",
                                    "entity_type": "neuron",
                                    "entity_name": "BasalGanglia",
                                    "description": "This is an extended description of the entity",
                                    "author": "Nathan Jordan",
                                    "author_email": "njordan@cse.unr.edu",
                                    "specification": {
                                    "type": "hh",
                                    "parameters": {
                                    "threshhold": {"type": "exact","value": 65.0},
                                    "resting_potential": { "type": "uniform", "min": -23.0, "max": -30.0},
                                    "capacitance": { "type": "exact", "value": 65.0},
                                    "channels": [
                                                 { "channel_id": "kfjdasfj90j90ahs90dhf", "count": 4},
                                                 { "channel_id": "jf890dash8sdghf89asghdf", "count": 4}]
                                    }}})
izhNeuron = connection.Izhikevich({
                                  "_id": "ajsd9fd90ha0hsd80fhd80sha",
                                  "entity_type": "neuron",
                                  "entity_name": "neuron_izh_1",
                                  "description": "This is an extended description of the entity",
                                  "author": "Nathan Jordan",
                                  "author_email": "njordan@cse.unr.edu",
                                  "specification": {
                                  "type": "izhikevich",
                                  "parameters": {"a": 0.02, "b": 0.2, "c": -65.0, "d": 8.0, "u": -12.0, "v": -65.0,"threshold": 30
                                  }}})

for x in range(0, 12):
    hhNeuron['_id'] = "hhNeuron" + str(x)
    izhNeuron['_id'] = "izhNeuron" + str(x)
    ncsNeuron['_id'] = "ncsNeuron" + str(x)
    hhNeuron.save()
    izhNeuron.save()
    ncsNeuron.save()

