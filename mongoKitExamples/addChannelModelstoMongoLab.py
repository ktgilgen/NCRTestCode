{
    "_id": "df90sahf0sd9ha8sdhf8dhsa",
    "entity_type": "channel",
    "entity_name": "channel_vg",
    "description": "This is an extended description of the entity",
    "author": "Nathan Jordan",
    "author_email": "njordan@cse.unr.edu",
    "channel_parameters": {
        "type": "voltage_gated",
        "conductance": {
            "type": "exact",
            "value": 65.0
        },
        "reversal_potential": {
            "type": "exact",
            "value": 65.0
        },
        "particles": {
	       	"x_initial": 5.0,
            "alpha": {
                "a": 0.5,
                "b": 0.01,
                "c": 1.0,
                "d": 50.0,
                "f": -10.0,
          		"h": -1.0,
            },
      		"beta": {
        		"a": 0.125,
          		"b": 0.0,
          		"c": 0.0,
          		"d": 60.0,
          		"f": 80.0,
          		"h": 1.0,
        	},
        	"power": 4.0,
        }	#particles
    } #chaanel params
}