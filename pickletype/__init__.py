def get_type(data):
    if isinstance(data, list):
        return [get_type(x) for x in data]
    elif isinstance(data, tuple):
        return tuple(get_type(x) for x in data)
    else:
        return type(data)
