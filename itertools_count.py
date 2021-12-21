def count(start=0, step=1):
    """
    Works as a function count in module itertools.
    Parameters 'start' and 'step' are defaulted.
    Returns generated numbers beginning from the start with exact step.
    :param start: int
    :param step: int
    :return: generator
    """
    if type(start) != int or type(step) != int:
        print('Incorrect input, only integers are allowed')
        exit()
    start_point = start
    while True:
        yield start_point
        start_point = start_point + step
