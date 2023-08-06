import os
import yaml
import json
from jsonschema import Draft7Validator, validators

with open(os.path.join(os.path.dirname(__file__), "schema.yaml"), "r") as f:
    schema = yaml.load(f, Loader=yaml.FullLoader)


def get(name):
    return schema['definitions'][name]


def extend_with_default(validator_class):
    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, schema):
        for property, subschema in properties.items():
            if "default" in subschema:
                instance.setdefault(property, subschema["default"])

        for error in validate_properties(
            validator, properties, instance, schema,
        ):
            yield error

    return validators.extend(
        validator_class, {"properties": set_defaults},
    )


DefaultValidatingDraft7Validator = extend_with_default(
    Draft7Validator)


def _init_schema(direction, definition):
    s = dict(get(definition))
    s['$schema'] = schema['$schema']
    s['definitions'] = schema['definitions']
    if direction == 'request':
        s = DefaultValidatingDraft7Validator(s)
    else:
        s = Draft7Validator(s)

    def validate(data):
        try:
            s.validate(data)
            return data
        except Exception:
            print("---")
            print(json.dumps(data, indent=2))
            print("---")
            raise
    return validate


validators = {
    'models': {
        'addon': _init_schema('request', 'Addon'),
        'item': {
            'directory': _init_schema('request', 'DirectoryItem'),
            'movie': _init_schema('request', 'MovieItem'),
            'series': _init_schema('request', 'SeriesItem'),
            'episode': _init_schema('request', 'EpisodeItem'),
            'channel': _init_schema('request', 'ChannelItem'),
            'iptv': _init_schema('request', 'IptvItem'),
            'basic': _init_schema('request', 'Item'),
        },
        'source': _init_schema('request', 'Source'),
        'subtitle': _init_schema('request', 'Subtitle'),
        'video': _init_schema('request', 'Video'),
        'apiError': _init_schema('request', 'ApiError'),
    },
    'actions': {
        'addons': {
            'addonType': 'repository',
            'request': _init_schema('request', 'ApiAddonsRequest'),
            'response': _init_schema('response', 'ApiAddonsResponse'),
        },
        'infos': {
            'addonType': None,
            'request': _init_schema('request', 'ApiInfosRequest'),
            'response': _init_schema('response', 'ApiInfosResponse'),
        },
        'directory': {
            'addonType': 'worker',
            'request': _init_schema('request', 'ApiDirectoryRequest'),
            'response': _init_schema('response', 'ApiDirectoryResponse'),
        },
        'metadata': {
            'addonType': 'worker',
            'request': _init_schema('request', 'ApiMetadataRequest'),
            'response': _init_schema('response', 'ApiMetadataResponse'),
        },
        'source': {
            'addonType': 'worker',
            'request': _init_schema('request', 'ApiSourceRequest'),
            'response': _init_schema('response', 'ApiSourceResponse'),
        },
        'subtitle': {
            'addonType': 'worker',
            'request': _init_schema('request', 'ApiSubtitleRequest'),
            'response': _init_schema('response', 'ApiSubtitleResponse'),
        },
        'resolve': {
            'addonType': 'worker',
            'request': _init_schema('request', 'ApiResolveRequest'),
            'response': _init_schema('response', 'ApiResolveResponse'),
        },
    },
    'task': {
        'task': _init_schema('response', 'ApiTask'),
        'result': _init_schema('request', 'ApiTaskResult'),
    },
}

for key in ['resolveVideo', 'resolveSource', 'resolveSubtitle']:
    validators['actions'][key] = validators['actions']['resolve']
