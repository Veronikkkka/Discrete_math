def combinations(r, n):
    """
    Returns n length subsequences of elements from the r.

    Parameters:
    r: iterable
    n: length of subsequence

    Returns:
    generator of combinations of the given iterable(r)

    >>> list(combinations('ABCD', 3))
    [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
    >>> list(combinations(['K', 'A', 'T', 'E'], 4))
    [('K', 'A', 'T', 'E')]
    >>> list(combinations(['B', 'R', 'E', 'N', 'D', 'I'], 7))
    []
    """
    length = len(r)
    if n == 0:
        yield tuple()
    elif n != 0:
        for idx in range(n - 1, length):
            for combi in combinations(r[:idx], n - 1):
                yield combi + (r[idx],)
list(combinations('ABCD', 3))
