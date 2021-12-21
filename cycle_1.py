def cycle(iterable):
    """
    Take an iterable object and return
    incidentally iterator with repeat
    elements from iterable object
    """
    if iterable not in {tuple, list, str}:
        raise TypeError('Incorrect input, only strings or numbers are allowed')
    res = []    
    for elem in iterable:
        yield elem
        res.append(elem)
    while True:
        for i in res:
            yield i


