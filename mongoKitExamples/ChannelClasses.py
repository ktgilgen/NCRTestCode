class CalciumDependentChannel(Document):
    __collection__ = 'Channels'
    __database__ = 'brainlab_test'
    structure = {
        '_id':basestring,
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'channel_parameters': {
            'type': basestring,
            'm_initial': {
                'type':basestring,
                'value': float
            },
            'reversal_potential': {
                'type':basestring,
                'value': float
            },
            'm_power': {
                'type':basestring,
                'value': float
            },
            'conductance': {
                'type':basestring,
                'value': float
            },
            'forward_scale': {
                'type':basestring,
                'value': float
            },
            'forward_exponent': {
                'type':basestring,
                'value': float
            },
            'backwards_rate': {
                'type':basestring,
                'value': float
            },
            'tau_scale': {
                'type':basestring,
                'value': float
        }
    }
    }
    required_fields=['_id']
    default_values={}


class VoltageGatedChannel(Document):
    __collection__ = 'Channels'
    __database__ = 'brainlab_test'
    structure = {
        '_id':basestring,
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'channel_parameters': {
            'type': basestring,
            'conductance': { 'type': basestring, 'value': float},
            'reversal_potential': { 'type': basestring, 'value':float},
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
    required_fields=['_id']
    default_values={}


class VoltageGAtedIonChannel(Document):
    __collection__ = 'Channels'
    __database__ = 'brainlab_test'
    structure = {
        '_id':basestring,
        'entity_type': basestring,
        'entity_name':basestring,
        'description': basestring,
        'author': basestring,
        'author_email': basestring,
        'channel_parameters': {
            'type': basestring,
            'v_half_active': { 'type':basestring, 'value':int},
            'transaction_rate': { 'type': basestring, 'value': int},
            'activation_slope': { 'type': basestring, 'value':int },
            'deactivation_slope': { 'type': basestring, 'value': int},
            'equilibrium_slope': { 'type': basestring, 'value': int},
            'conductance': { 'type': basestring, 'value': int},
            'reversal_potential': { 'type': basestring, 'value':int},
            'm_initial': { 'type': basestring, 'value': int},
            'm_power':{ 'type': basestring, 'value' : float}
            
        }
    }
    required_fields=['_id']
    default_values={}

