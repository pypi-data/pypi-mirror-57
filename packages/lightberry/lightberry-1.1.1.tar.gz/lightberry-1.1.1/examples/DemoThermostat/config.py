import os

import yaml

file = os.getenv('LIGHTBERRY_CONFIG', 'config.yaml')


class DotDict(dict):
    """
    a dictionary that supports dot notation
    as well as dictionary access notation
    usage: d = DotDict() or d = DotDict({'val1':'first'})
    set attributes: d.val2 = 'second' or d['val2'] = 'second'
    get attributes: d.val2 or d['val2']
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, dct, **kwargs):
        super().__init__(**kwargs)
        for key, value in dct.items():
            if hasattr(value, 'keys'):
                value = DotDict(value)
            self[key] = value


with open(file, 'r') as f:
    __options__ = DotDict(yaml.safe_load(f))


def __getattr__(key):
    return __options__.get(key)
