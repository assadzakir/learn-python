# collections module counter

from collections import Counter

print('=============================================')

num_l = [1, 1, 1, 2, 4, 5, 5, 4, 6, 4, 8, 65, 5, 132, 321, 4, 4, 5, 4, ]

print(Counter(num_l))  # {4: 6, 5: 4, 1: 3, 2: 1, 6: 1, 8: 1, 65: 1, 132: 1, 321: 1}

print('=============================================')

str_l = ['a', 'b', 'c', 'a']

print(Counter(str_l))  # {'a': 2, 'b': 1, 'c': 1}

print('=============================================')

_sen = 'The The quick quick brown fox jumps over the lazy dog'.split()

print(
    Counter(_sen))  # {'The': 2, 'quick': 2, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog': 1}

print(Counter(_sen).most_common(2))  # ('The', 2), ('quick', 2)

print(Counter(_sen).values())  # [2, 2, 1, 1, 1, 1, 1, 1, 1]
