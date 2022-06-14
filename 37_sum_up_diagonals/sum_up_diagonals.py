def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
#     list_A = []
#     list_B = []
#     for num in range(len(matrix)):
#         list_A.append(matrix[num][num])        
#         list_B.append(matrix[num][-1 - num])        
#     print(list_A)
#     print(list_B)
#     return sum(list_A) + sum(list_B)

# m1 = [
#     [1,   2],
#     [30, 40],
#     ]

# m2 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     ]

    total = 0
    for num in range(len(matrix)):
        total += matrix[num][num]
        total += matrix[num][-1 - num]

    return total