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


connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)
connection.register([Group])

item = connection.Group({
"_id": "df90sahf0sd9ha8sdhf8dhsa", 
"entity_type": "group",
"entity_name": "BasalGanglia",
"description": "This is an extended description of the entity",
"author": "Nathan Jordan",
"author_email": "njordan@cse.unr.edu",
"geometry": {
"width": 100,
"height": 200,
"depth": 300
},
"subgroups": [
              {
"model_id": "sdfh8ahsdf80has0d89fh0as9dhf",
"label": "Striatum",
"location": {"x": 123,"y": 456,"z": 789}
              },
              {
"model": "hf8as0df8asdhf80ahsd80f",
"label": "Pallidum",
"location": {"x": 234,"y": 456,"z": 543}
              }
              ],
"neuron_groups": [
{
"neuron": "hfd80sahs80dhf0shda90fhshdf",
"label": "GPe",
"geometry": {
"width": 100,
"height": 200,
"depth": 300
},
"location": {
"x": 234,
"y": 456,
"z": 543}
                  },
{
"neuron": "hasd890fhas80fhas80dhf",
"label": "GPi",
"geometry": {
"width": 100,
"height": 200,
"depth": 300
},
"location": {
"x": 784,
"y": 926,
"z": 999
}
}
],
"aliases": {
"model_aliases": [
{
"alias": "GPx",
"labels": [
"GPe",
"GPi"
]
}
],
"synaptic_aliases": [
                     {"alias": "sample_synapse_alias",
                     "labels": ["GP_synapse"]}
                     ]},
"connections": [
                
                {
"presynaptic": "GPe",
"postsynaptic": "GPi",
"probability": 0.5,
"synapse": "hfd8nfiodnsa80dbhfbas80df",
"recurrent": "false"
                },
                {
"presynaptic": "GPe:Excitatory_Cells_1",
"postsynaptic": "GPx:[Inhibitory]",
"probability": 0.5,
"synapse": "nfd8s0ahfd80ba80sbdfbd8sba",
"recurrent": "false"
                },
                {
"presynaptic": "GPi:[Inhibitory]",
"postsynaptic": "GPi:{Excitatory}",
"probability": 0.5,
"synapse": "nfd0sahf80hasdhf80dhsa",
"recurrent": "false"
                }
                ]
                 })

for x in range (0, 10):
    item['_id'] = str(x)
    item.save()