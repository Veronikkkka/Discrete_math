
def permutations(iterable, length=None):
    """
    Return successive n length(second arg) permutations of elements in the iterable.

    If r is not specified, then length defaults to the length of the iterable
    and all possible full-length permutations are generated.

    Parameters:
    iterable: array or string to be iterated by function
    length: length of subsequence

    Returns:
    generator of permutations of the given iterable

    >>> list(permutations('ABCD', 3))
    [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]

    >>> list(permutations(['K', 'A', 'T', 'E'], 4))
    [('K', 'A', 'T', 'E'), ('K', 'A', 'E', 'T'), ('K', 'T', 'A', 'E'), ('K', 'T', 'E', 'A'), ('K', 'E', 'A', 'T'), ('K', 'E', 'T', 'A'), ('A', 'K', 'T', 'E'), ('A', 'K', 'E', 'T'), ('A', 'T', 'K', 'E'), ('A', 'T', 'E', 'K'), ('A', 'E', 'K', 'T'), ('A', 'E', 'T', 'K'), ('T', 'K', 'A', 'E'), ('T', 'K', 'E', 'A'), ('T', 'A', 'K', 'E'), ('T', 'A', 'E', 'K'), ('T', 'E', 'K', 'A'), ('T', 'E', 'A', 'K'), ('E', 'K', 'A', 'T'), ('E', 'K', 'T', 'A'), ('E', 'A', 'K', 'T'), ('E', 'A', 'T', 'K'), ('E', 'T', 'K', 'A'), ('E', 'T', 'A', 'K')]

    >>> list(permutations(['B', 'R', 'E', 'N', 'D', 'I'], 7))
    []
    """
    if length is None:
        length = len(iterable)

    if length > len(iterable):
        return

    indexes_of_eles = []
    for i in range(len(iterable)):
        indexes_of_eles.append(i)

    cycles = []
    for i in range(len(iterable), len(iterable)-length, -1):
        cycles.append(i)

    yield tuple(iterable[i] for i in indexes_of_eles[:length])

    while len(iterable) != 0:
        for idx in range(length)[::-1]:
            cycles[idx] -= 1
            if cycles[idx] != 0:
                j = cycles[idx]
                indexes_of_eles[idx], indexes_of_eles[-j] = indexes_of_eles[-j], indexes_of_eles[idx]
                yield tuple(iterable[i] for i in indexes_of_eles[:length])
                break
            elif cycles[idx] == 0:
                indexes_of_eles[idx:] = indexes_of_eles[idx + 1:] + indexes_of_eles[idx:idx + 1]
                cycles[idx] = len(iterable) - idx
        else:
            return
