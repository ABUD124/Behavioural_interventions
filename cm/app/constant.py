CELERY_BROKER_URL_DOCKER = 'amqp://admin:mypass@rabbit:5672/'
CELERY_BROKER_URL_LOCAL = 'amqp://localhost/'

CM_REGISTER_Q = 'rpc_queue_CM_register'  # Do not change this value

CM_NAME = 'CM - Behavioural interventions'
RPC_CM_ALIVE = 'rpc_queue_CM_ALIVE'  # Do not change this value
RPC_Q = 'rpc_queue_CM_compute'  # Do not change this value
CM_ID = 14  # CM_ID is defined by the energy research center of Martigny (CREM)
PORT_LOCAL = int('500' + str(CM_ID))
PORT_DOCKER = 80

# TODO ********************setup this URL depending on which version you are running***************************

CELERY_BROKER_URL = CELERY_BROKER_URL_DOCKER
PORT = PORT_DOCKER

# TODO ********************setup this URL depending on which version you are running***************************
TRANFER_PROTOCOLE = 'http://'
# =============================================================================
#
# =============================================================================


INPUTS_CALCULATION_MODULE = [
    {
        'cm_id': CM_ID,
        'input_max': '',
        'input_min': '',
        'input_name': 'Field of intervention',
        'input_parameter_name': 'field_of_intervention',
        'input_type': 'select',
        'input_unit': '',
        'input_value': ['All', 'Occupant presence', 'Equipment use', 'Thermostat settings',
                        'Perceived thermal comfort and adaptation', 'Space cooling set-point preferences and schedules',
                        'Window opening and ventilation strategies', 'Shading types and operation']
    },
    {
        'cm_id': CM_ID,
        'input_max': '',
        'input_min': '',
        'input_name': 'Intervention type',
        'input_parameter_name': 'intervention_type',
        'input_type': 'select',
        'input_unit': '',
        'input_value': ['All', 'Monetary incentives', 'Providing feedback and information',
                        'Nudging occupants', 'Policy']
    },
    {
       'cm_id': CM_ID,
        'input_max': '',
        'input_min': '',
        'input_name': 'Building type',
        'input_parameter_name': 'building_type',
        'input_type': 'select',
        'input_unit': '',
        'input_value': ['All', 'Residential', 'Non-residential']
    }

]


# Define the SIGNATURE dictionary
SIGNATURE = {
    "category": "Demand",
    "cm_name": CM_NAME,
    "wiki_url": "",
    "layers_needed": [],
    "type_layer_needed": [{"type": "nuts_id_number", "description": "A default layer is used here."}],
    "type_vectors_needed": [],
    "cm_url": "Do not add something",
    "cm_description":
    "This calculation module allows the user"\
    "to filter behavioural interventions that help "\
    "reduce SC demand.",
    "cm_id": CM_ID,
    "inputs_calculation_module": INPUTS_CALCULATION_MODULE,
    "authorized_scale": ["NUTS 0"]
}
