def repeat(value, times=None):
    """
    Returns an infinite iterator of duplicate values value
    >>> list(repeat('ABC', 3))
    ['ABC', 'ABC', 'ABC']
    """
    if isinstance(times, int) and type(value) in {str, list, tuple}:
        if times is None:
            while True:
                yield value
        else:
            for i in range(times):
                yield value
    else:
        print(f'The type of parameter times is not integer "{times}"')
