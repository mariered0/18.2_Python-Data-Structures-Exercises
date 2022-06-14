def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    # if type(collection) == str or type(collection) == list or type(collection) == tuple:
    #     if start:
    #         check = collection[start:len(collection):]
    #         if sought in check:
    #             return True
    #         else:
    #             return False
    #     elif not start:
    #         if sought in collection:
    #             return True
    #         else:
    #             return False
    # elif type(collection) == set:
    #     if sought in collection:
    #         return True
    #     else:
    #         return False
    # elif type(collection) == dict:
    #     check = collection.values()
    #     if sought in check:
    #         return True
    #     else:
    #         return False

    if isinstance(collection, dict):
        return sought in collection.values()
    
    elif start is None or isinstance(collection, set):
        return sought in collection
    
    return sought in collection[start:]
    

        