# zip(*iterables)

# Make an iterator that aggregates elements from each of the iterables.

# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences
# or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument,
# it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. Equivalent to:

print('=============================================')

x = [1, 2, 3]
y = [4, 5, 6]

print(list(zip(x, y)))  # [(1, 4), (2, 5), (3, 6)]

print('=============================================')

a = range(0, 11)
b = range(12, 21)

print(list(zip(a, b)))  # [(0, 12), (1, 13), (2, 14), (3, 15), (4, 16), (5, 17), (6, 18), (7, 19), (8, 20)]

print('=============================================')

for pair in zip(a, b):
    print(max(pair))  # 12, 13, 14, 15, 16, 17, 18, 19,20

print('=============================================')

print(list(map(lambda pair: max(pair), zip(a, b))))  # [12, 13, 14, 15, 16, 17, 18, 19, 20]

print('=============================================')

c = [1, 2, 3]
d = [4, 2, 3, 5, 8]

print(list(zip(c, d)))  # [(1, 4), (2, 2), (3, 3)]

print('=============================================')

print(list(zip(d, c)))  # [(4, 1), (2, 2), (3, 3)]

print('=============================================')

d_1 = {'a': 1, 'b': 2}
d_2 = {'c': 3, 'd': 4}

print(list(zip(d_1.values(), d_2.values())))  # [(1, 3), (2, 4)]

print(list(zip(d_1, d_2)))  # [('a', 'c'), ('b', 'd')]

print('=============================================')


def switcharoo(d1, d2):
    dout = {}

    for d1key, d2val in zip(d_1, d_2.values()):
        dout[d1key] = d2val

    return dout


print(switcharoo(d_1, d_2))  # {'a': 3, 'b': 4}


# Note
# This is an advanced function that is not needed in everyday Python programming,
# unlike importlib.import_module().
