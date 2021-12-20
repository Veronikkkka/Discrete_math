def cycle(iterable):
    """
    Take an iterable object and return
    incidentally iterator with repeat
    elements from iterable object
    """
    res = []    
    for elem in iterable:
        yield elem
        res.append(elem)
    while True:
        for i in res:
            yield i


