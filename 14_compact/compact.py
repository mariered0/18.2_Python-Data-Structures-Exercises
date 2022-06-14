def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # copy = []
    # for el in lst:
    #     if el:
    #         copy.append(el)
    # return copy

    return [el for el in lst if el]