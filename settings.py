from os import environ

ROBOFLOW_API_KEY = environ.get('ROBOFLOW_API_KEY')
FLASK_DEBUG = environ.get('FLASK_DEBUG')
PORT = environ.get('PORT')
TF_ENABLE_ONEDNN_OPTS = environ.get('TF_ENABLE_ONEDNN_OPTS')
