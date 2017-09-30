# reduce

from functools import reduce

print('=============================================')

l = [1, 2, 3]

print(max(l))  # 3

print('=============================================')


def find_max(a, b):
    if a > b:
        return a
    else:
        return b


print(find_max(100, 1200))  # 1200

print('=============================================')

print(reduce(find_max, l))  # 3

print('=============================================')

print(reduce((lambda x, y: x + y), l))  # 6
