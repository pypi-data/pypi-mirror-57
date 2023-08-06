import os
import json
import jsonschema

__configurations_file_path = './configurations.json'
__loaded_configurations = None


def __load_configurations():
    global __loaded_configurations

    if __loaded_configurations is not None:
        return

    if not os.path.exists(__configurations_file_path):
        raise FileExistsError("Configuration file '%s' not found" % __configurations_file_path)

    with open(__configurations_file_path) as json_file:
        __loaded_configurations = json.load(json_file)


def __validate_configurations():
    global __loaded_configurations

    if __loaded_configurations is None:
        raise ImportError("Can't validate configurations (Not loaded yet")

    schema_file_path = os.path.dirname(os.path.realpath(__file__)) + '/configurationSchema.json'

    with open(schema_file_path) as json_file:
        schema = json.load(json_file)

        jsonschema.validate(instance=__loaded_configurations, schema=schema)


def get(module, key):
    global __loaded_configurations

    if __loaded_configurations is None:
        __load_configurations()
        __validate_configurations()

    if module not in __loaded_configurations:
        raise KeyError("Configuration module '%s' not found" % module)

    if key not in __loaded_configurations[module]:
        raise KeyError("Configuration '%s' not found under module '%s'" % (key, module))

    return __loaded_configurations[module][key]
