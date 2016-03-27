class List(object):

    def __init__(self, typ):
        self.typ = typ

    def __eq__(self, rhs):
        return isinstance(rhs, List) and rhs.typ == self.typ

    def __str__(self):
        return 'list({})'.format(self.typ)


class Dict(object):
    def __init__(self, key_type, value_type):
        self.key_type = key_type
        self.value_type = value_type

    def __eq__(self, rhs):
        return (isinstance(rhs, Dict) and
                rhs.key_type == self.key_type and
                rhs.value_type == self.value_type)

    def __str__(self):
        return 'dict({}, {})'.format(self.key_type, self.value_type)


def get_type(data):
    if isinstance(data, list):
        typs = [get_type(x) for x in data]
        if len(typs) > 1 and all(t == typs[0] for t in typs):
            return List(typs[0])
        else:
            return typs

    elif isinstance(data, tuple):
        return tuple(get_type(x) for x in data)

    elif isinstance(data, dict):
        key_types = [get_type(k) for k in data.keys()]
        value_types = [get_type(v) for v in data.values()]
        if len(data) > 0 and \
           all(t == key_types[0] for t in key_types[1:]) and \
           all(t == value_types[0] for t in value_types[1:]):
            return Dict(key_types[0], value_types[0])
        else:
            return dict

    else:
        return type(data)
