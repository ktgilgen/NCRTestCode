import pymongo
from mongokit import *
import datetime
import json

class Group(Document):
    __collection__ = 'Neuron_Group'
    __database__ = 'brainlab_test'
    structure = {
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'specification' : {
            'geometry': {'width': float, 'height': float, 'depth': float},
            'subgroups':    [{
                           'group': basestring, 'label': basestring, 
                           'location': {'x': float, 'y': float, 'z': float}
                              }] ,
            'neuron_groups': [{ 
                              'neuron': basestring, 'label': basestring,   
                            'geometry': { 'width': float, 'height': float, 'depth': float},
                            'location': { 'x': float, 'y': float, 'z': float}
                              }]  ,
            'neuron_aliases': [{ 
                               'alias' :  basestring, 'labels' : [basestring], 'aliases' : [basestring]
                               }] ,
            'synaptic_aliases' : [{
                                  'alias' : basestring, 'labels' : [basestring]
                               }] ,
            'connections': [{ 
                            'presynaptic': basestring, 'postsynaptic': basestring,
                        'probability': float, 'synapse': basestring, 'recurrent': basestring
                            }]
        }
    }


connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)
connection.register([Group])



for x in range (0, 10):
    item = connection.Group({
                            "entity_type": "group",
                            "entity_name": "BasalGanglia",
                            "description": "This is an extended description of the entity",
                            "author": "Nathan Jordan",
                            "author_email": "njordan@cse.unr.edu",
                            "specification": {
                            "geometry": {
                            "width": 100.0,
                            "height": 200.7,
                            "depth": 300.3
                            },
                            "subgroups": [
                                          {
                                          "group": "sdfh8ahsdf80has0d89fh0as9dhf",
                                          "label": "striatum",
                                          "location": {
                                          "x": 123.5,
                                          "y": 456.5,
                                          "z": 789.5
                                          }
                                          },
                                          {
                                          "group": "hf8as0df8asdhf80ahsd80f",
                                          "label": "pallidum",
                                          "location": {
                                          "x": 2354.5,
                                          "y": 456.5,
                                          "z": 543.5
                                          }
                                          }
                                          ],
                            "neuron_groups": [
                                              {
                                              "neuron": "hfd80sahs80dhf0shda90fhshdf",
                                              "label": "gpe",
                                              "geometry": {
                                              "width": 100.4,
                                              "height": 200.7,
                                              "depth": 300.8
                                              },
                                              "location": {
                                              "x": 234.9,
                                              "y": 456.4,
                                              "z": 543.2
                                              }
                                              },
                                              {
                                              "neuron": "hasd890fhas80fhas80dhf",
                                              "label": "gpi",
                                              "geometry": {
                                              "width": 100.1,
                                              "height": 200.6,
                                              "depth": 300.7
                                              },
                                              "location": {
                                              "x": 784.4,
                                              "y": 926.1,
                                              "z": 999.2
                                              }
                                              }
                                              ],
                            "neuron_aliases": [
                                               {
                                               "alias": "gpx",
                                               "labels": [
                                                          "gpe",
                                                          "gpi"
                                                          ],
                                               "aliases": [
                                                           "an_alias"
                                                           ]
                                               }
                                               ],
                            "synaptic_aliases": [
                                                 {
                                                 "alias": "sample_synapse_alias",
                                                 "labels": [
                                                            "GP_synapse"
                                                            ]
                                                 }
                                                 ],
                            "connections": [
                                            {
                                            "presynaptic": "gpe",
                                            "postsynaptic": "gpi",
                                            "probability": 0.5,
                                            "synapse": "hfd8nfiodnsa80dbhfbas80df",
                                            "recurrent": "false"
                                            }
                                            ]
                            }
                            })
    item['entity_name'] = "group" + str(x)
    if x % 3 == 0:
        item['author'] = "Riley Carroll"
    elif x % 4 == 0:
        item['author'] = "Thor Kvarna"
    item.save()