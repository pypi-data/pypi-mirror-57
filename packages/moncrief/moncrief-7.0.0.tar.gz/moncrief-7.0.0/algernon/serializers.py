import importlib
import json
from datetime import datetime, timedelta, tzinfo
from decimal import Decimal

import pytz
from jsonref import JsonRef
import rapidjson

from algernon.alg_obj import AlgObject


class ExplosionJson:
    @classmethod
    def loads(cls, json_string):
        return rapidjson.loads(json_string, object_hook=ExplosionDecoder.object_hook)


class AlgJson:
    @classmethod
    def loads(cls, json_string):
        return rapidjson.loads(json_string, object_hook=AlgDecoder.object_hook)

    @classmethod
    def dumps(cls, obj):
        return rapidjson.dumps(obj, default=AlgEncoder.default)


class AlgEncoder(json.JSONEncoder):
    @classmethod
    def default(cls, obj):
        if isinstance(obj, AlgObject):
            return {'_alg_class': type(obj).__name__, '_alg_module': str(obj.__module__), 'value': obj.to_json}
        if isinstance(obj, frozenset):
            list_value = [x for x in obj]
            return {'_alg_class': 'frozenset', 'value': list_value}
        if isinstance(obj, set):
            list_value = [x for x in obj]
            return {'_alg_class': 'set', 'value': list_value}
        if isinstance(obj, tuple):
            return {'_alg_class': 'tuple', 'value': obj}
        if isinstance(obj, datetime):
            if obj.tzinfo is None:
                raise RuntimeError(f'algernon does not support serializing and deserializing of naive datetimes: {obj}')
            if obj.tzinfo != pytz.UTC:
                raise RuntimeError(f'algernon only support serializing and deserializing UTC aware datetimes: {obj}')
            return {'_alg_class': 'datetime', 'value': {'tz': 'UTC', 'timestamp': obj.timestamp()}}
        if isinstance(obj, Decimal):
            return {'_alg_class': 'decimal', 'value': str(obj)}
        if isinstance(obj, JsonRef):
            subject = obj.__subject__
            return subject
        return super(AlgEncoder, cls()).default(obj)


class AlgDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    @staticmethod
    def object_hook(obj):
        if '_alg_class' not in obj:
            return obj
        alg_class = obj['_alg_class']
        obj_value = obj['value']
        if alg_class == 'frozenset':
            return frozenset(x for x in obj_value)
        if alg_class == 'set':
            return set(x for x in obj_value)
        if alg_class == 'tuple':
            return tuple(x for x in obj_value)
        if alg_class == 'datetime':
            tz_info = obj_value['tz']
            timestamp = obj_value['timestamp']
            if tz_info is None:
                raise RuntimeError(f'algernon does not support serializing and deserializing of naive datetimes: {obj}')
            if tz_info != 'UTC':
                raise RuntimeError(f'algernon is very picky about dates, will only decode UTC aware datetimes: {obj}')
            return datetime(1970, 1, 1, tzinfo=pytz.UTC) + timedelta(seconds=timestamp)
        if alg_class == 'decimal':
            return Decimal(obj_value)
        if '_alg_module' not in obj:
            return obj
        alg_module = obj['_alg_module']
        host_module = importlib.import_module(alg_module)
        obj_class = getattr(host_module, alg_class, None)
        if obj_class is None:
            raise RuntimeError(f'alg_class: {alg_class}, in alg_module: {alg_module} could not be located')
        return obj_class.from_json(obj_value)


class GqlDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    @staticmethod
    def object_hook(obj):
        if '_alg_class' not in obj:
            return obj
        alg_class = obj['_alg_class']
        obj_value = obj['value']
        if alg_class == 'frozenset':
            return frozenset(x for x in obj_value)
        if alg_class == 'tuple':
            return tuple(x for x in obj_value)
        if alg_class == 'datetime':
            return str(obj_value)
        if alg_class == 'decimal':
            return Decimal(obj_value)
        if '_alg_module' not in obj:
            return obj
        alg_module = obj['_alg_module']
        host_module = importlib.import_module(alg_module)
        obj_class = getattr(host_module, alg_class, None)
        if obj_class is None:
            return obj
        alg_obj = obj_class.from_json(obj_value)
        return alg_obj.to_gql


class ExplosionDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    @staticmethod
    def object_hook(obj):
        if isinstance(obj, dict):
            if 'S' in obj:
                return str(obj['S'])
            if 'M' in obj:
                return obj['M']
            if 'BOOL' in obj:
                return bool(obj['BOOL'])
            if 'NULL' in obj:
                return None
            if 'N' in obj:
                return Decimal(obj['N'])
            if 'L' in obj:
                return list(obj['L'])
            if 'SS' in obj:
                return set(obj['SS'])
            return obj
        return obj


class TaskDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    @staticmethod
    def object_hook(obj):
        if '_alg_class' not in obj:
            return obj
        alg_class = obj['_alg_class']
        obj_value = obj['value']
        if 'S' in obj:
            return str(obj['S'])
        if 'M' in obj:
            return obj['M']
        if 'BOOL' in obj:
            return bool(obj['BOOL'])
        if 'NULL' in obj:
            return None
        if 'N' in obj:
            return Decimal(obj['N'])
        if 'L' in obj:
            return list(obj['L'])
        return obj
