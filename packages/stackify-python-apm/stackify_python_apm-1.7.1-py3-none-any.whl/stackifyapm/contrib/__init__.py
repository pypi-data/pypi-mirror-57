import json
import os

from stackifyapm.base import Client
from stackifyapm.conf import setup_logging
from stackifyapm.conf import constants
from stackifyapm.instrumentation.control import instrument


def make_client(**defaults):
    config_file = defaults.get("CONFIG_FILE") or defaults.get("config_file") or constants.DEFAULT_CONFIG_FILE
    application_name = defaults.get("APPLICATION_NAME") or defaults.get("application_name") or constants.DEFAULT_APPLICATION_NAME
    environment = defaults.get("ENVIRONMENT") or defaults.get("environment") or constants.DEFAULT_ENVIRONMENT
    base_dir = defaults.get("BASE_DIR") or defaults.get("base_dir") or os.getcwd()
    multiprocessing = defaults.get("MULTIPROCESSING") or defaults.get("multiprocessing") or constants.DEFAULT_MULTIPROCESSING
    transport = defaults.get("TRANSPORT") or defaults.get("transport") or constants.DEFAULT_TRANSPORT
    http_endpoint = defaults.get("HTTP_ENDPOINT") or defaults.get("http_endpoint") or constants.DEFAULT_HTTP_ENDPOINT

    try:
        with open(config_file) as json_file:
            data = json.load(json_file)
            application_name = data.get('application_name') or application_name
            environment = data.get('environment') or environment
            base_dir = data.get('base_dir') or base_dir
            multiprocessing = data.get('multiprocessing') or multiprocessing
            transport = data.get('transport') or transport
            http_endpoint = data.get('http_endpoint') or http_endpoint
    except Exception:
        pass

    config = {
        "APPLICATION_NAME": application_name,
        "ENVIRONMENT": environment,
        "BASE_DIR": base_dir,
        "CONFIG_FILE": config_file,
        "MULTIPROCESSING": multiprocessing,
        "TRANSPORT": transport,
        "HTTP_ENDPOINT": http_endpoint,
    }

    return Client(config, **defaults)


class StackifyAPM(object):
    """
    Generic application for StackifyAPM.
    """
    def __init__(self, **defaults):
        setup_logging()
        self.client = make_client(**defaults)
        instrument(self.client)

    def clean_up(self):
        self.client.transport.send_all()
