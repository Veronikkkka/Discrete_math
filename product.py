import itertools


def product(*iterables, repeat=1):
    """Returns the generator of the Cartesian
    product of given objects

    :param repeat: how many times to repeat arguements, defaults to 1
    :type repeat: int, optional
    :raises TypeError: error caused by invalid types of arguement
    :return: generator of the Cartesian product
    :rtype: <class 'generator'>
    :yield: one objects from the product
    :rtype: tuple
    >>> list(product('AB', '12', '1'))
    [('A', '1', '1'), ('A', '2', '1'), ('B', '1', '1'), ('B', '2', '1')]
    >>> list(product())
    [()]
    >>> list(product('AB'))
    [('A',), ('B',)]
    >>> list(product('A', '1'))
    [('A', '1')]
    >>> list(product('AB', repeat=2))
    [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
    >>> len(list(product('00', repeat=10)))
    1024
    >>> len(list(product('00', repeat=20)))
    1048576
    >>> list(product(1, 23))
    [('1', '2'), ('1', '3')]
    """
    type_check = list(filter(lambda x: type(x) in {int, float, str}, iterables))
    if len(type_check) < len(iterables):
        raise TypeError('Incorrect input, only strings or numbers are allowed')
    
    objects = list(map(str, iterables)) * repeat

    def cycle(prod_elem, objects_iter):
        """
        Generator, which iterates on two levels, combining the product
        """        
        for begin in objects_iter:
            for finish in prod_elem:
                yield tuple(list(begin) + list(finish))

    result = iter((tuple(),))
    for object in objects:
        result = cycle(object, result)  # build stack of iterators
    return result


# from time import time
# start1 = time()
# list(product('ABCD', repeat=10))
# start2 = time()
# list(itertools.product('ABCD', repeat=10))
# finish = time()
# print(start2-start1)
# print(finish-start2)
