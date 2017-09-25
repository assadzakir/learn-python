# Python: List Comprehensions

# Python supports a concept called "list comprehensions".
# It can be used to construct lists in a very natural, easy way, like a mathematician is used to do.

# The following are common ways to describe lists (or sets, or tuples, or vectors) in mathematics.

# S = {x² : x in {0 ... 9}}
# V = (1, 2, 4, 8, ..., 2¹²)
# M = {x | x in S and x even}


print('=============================================')

l = []

for letter in 'numbers':
    l.append(letter)

print(l)  # ['n', 'u', 'm', 'b', 'e', 'r', 's']

print('=============================================')

list = [letter for letter in 'numbers']

print(list)  # ['n', 'u', 'm', 'b', 'e', 'r', 's']

print('=============================================')

list_2 = [x * 2 for x in range(10)]

print(list_2)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print('=============================================')

list_3 = [x for x in range(10) if x % 2 == 0]

print(list_3)  # [0, 2, 4, 6, 8]

print('=============================================')

list_4 = [x * 2 for x in [x * 2 for x in range(10)]]

print(list_4)  # [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]

print('=============================================')
