def combinations_with_replacement(elements, number):
    """
    Returns the generator of all combinations from n to r elements with repetitions in sorted order
    >>> list(combinations_with_replacement('ABC', 2))
    [('A', 'A'), ('A', 'C'), ('A', 'B'), ('C', 'C'), ('C', 'B'), ('B', 'B')]
    >>> list(combinations_with_replacement([7, 9], 3))
    [(7, 7, 7), (7, 7, 9), (7, 9, 9), (9, 9, 9)]
    """
    if type(elements) not in {tuple, list, str}:
        raise TypeError('Incorrect input, only strings, tuples or lists are allowed')
    elif type(number) != int:
        raise TypeError('Incorrect input, only integers are allowed')
    else:
        length = len(elements)
        cells = [0] * number
        if length == 0 or number == 0:
            return
        lst = []
        for k in cells:
            lst.append(elements[k])
        yield tuple(lst)
        while True:
            for i in range(number - 1, -1, -1):
                if cells[i] != length - 1:
                    break
            else:    
                break
            cells[i:] = [cells[i] + 1] * (number - i)
            lst = []
            for k in cells:
                lst.append(elements[k])
            yield tuple(lst)
