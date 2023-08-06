VERSION = (0, 2, 0)


def get_version():
    """
    Returns the version in a human-format string.
    """
    return '.'.join([str(i) for i in VERSION])
