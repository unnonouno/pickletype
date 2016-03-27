class List(object):

    def __init__(self, typ):
        self.typ = typ

    def __eq__(self, rhs):
        return isinstance(rhs, List) and rhs.typ == self.typ


def get_type(data):
    if isinstance(data, list):
        typs = [get_type(x) for x in data]
        if len(typs) > 1 and all(t == typs[0] for t in typs):
            return List(typs[0])
        else:
            return typs

    elif isinstance(data, tuple):
        return tuple(get_type(x) for x in data)
    else:
        return type(data)
