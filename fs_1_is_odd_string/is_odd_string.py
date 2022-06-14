def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here

    # to_sum = []
    # for char in word:
    #     to_sum.append(ord(char))
        
    # return not sum(to_sum) % 2 == 0

    to_sum = []
    for char in word:
        alp = 'abcdefghijklmnopqrstuvwxyz'
        num = alp.index(char.lower()) +1
        to_sum.append(num)

    return sum(to_sum) % 2 == 1
    

