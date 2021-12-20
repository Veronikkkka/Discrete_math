def combinations_with_replacement(elements, number):
    """
    Returns the generator of all combinations from n to r elements with repetitions in sorted order
    >>> list(combinations_with_replacement('ABC', 2))
    [('A', 'A'), ('A', 'C'), ('A', 'B'), ('C', 'C'), ('C', 'B'), ('B', 'B')]
    >>> list(combinations_with_replacement([7, 9], 3))
    [(7, 7, 7), (7, 7, 9), (7, 9, 9), (9, 9, 9)]
    """
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
            return
        cells[i:] = [cells[i] + 1] * (number - i)
        lst = []
        for k in cells:
            lst.append(elements[k])
        yield tuple(lst)

