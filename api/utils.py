import json


def prepare_obj_dict(model, fields, fields_renaming=None):
    fields_renaming = {} if fields_renaming is None else fields_renaming
    serialized = {}
    for field in fields:
        renamed_field = fields_renaming.get(field) or field
        serialized[renamed_field] = model.__dict__.get(field)

    return serialized


def prepare_query(query, fields, fields_renaming=None):
    objs = [
        prepare_obj_dict(model, fields, fields_renaming) for model in query
    ]

    return objs


def dump_query(query, fields, fields_renaming=None):
    return json.dumps(prepare_query(query, fields, fields_renaming))


def dump_obj(obj, fields, fields_renaming=None):
    return json.dumps(prepare_obj_dict(obj, fields, fields_renaming))

