# https://stackoverflow.com/a/4015104


from functools import wraps


class MessageDict(dict):
    """
    This class implements a dictionary, which make use of event sourcing over
    networking with rabbitMQ, so the developer can use a in memory dictionary,
    which replicate itself in other microservice.

    If one value in this dict is changed, it emits a message to rabbitMQ and any
    other consumer will get this change and modify the dict by itself.

    This dict should only be used, if you want to use `--replica` in kubernetes
    for the container, where this dict is running in.
    """

    def __init__(self, *arg, **kw):
        super(MessageDict, self).__init__(*arg, **kw)

    def __setitem__(self, key, item):
        super(MessageDict, self).__setitem__(key, item)

    def __delitem__(self, key):
        super(MessageDict, self).__delitem__(key)


def patch_all_dict(connection, unique_name):
    """
    This function patches all needed method from dict, so it can replicate
    itself over network into other microservices.

    FIXME Not working, because builtin structures are in c and cannot be monkeypatched.
    """
    dict.__setitem__ = add_channel(connection, f"{unique_name}.__setitem__")
    dict.__delitem__ = add_channel(connection, f"{unique_name}.__delitem__")


def add_channel(connection, channel_name, producer=True):
    def decorator(method):
        def wrapper(*args, **kwargs):
            # if this method produces messages

            # else this is a consumer

            result = method(*args, **kwargs)
            return result
        return wrapper
    return decorator
