# collections module namedtuple

# A named tuple is exactly like a normal tuple,
# except that the fields can also be accessed by .fieldname.
# Named tuples are still immutable,
# you can still index elements with integers,
# and you can iterate over the elements.

from collections import namedtuple

print('=============================================')

#  standard tuple
t = (1, 2, 3)

print(t[0])  # 1

print('=============================================')

# Example 1
Dog = namedtuple('Dog', 'age breed name')

tomy = Dog(age=2, breed='lab', name='tomy')

print(tomy)  # Dog(age=2, breed='lab', name='tomy')

print(tomy.name)  # tomy

print(tomy[2])  # tomy

print(tomy)  # Dog(age=2, breed='lab', name='tomy')

print('=============================================')

# Example 2

Cat = namedtuple('Cat', 'age  name food')

mamo = Cat(age=2, food='milk', name='mamo')

print(mamo)  # Cat(age=2, name='mamo', food='milk')

print(mamo.name)  # mamo

print(mamo[2])  # milk

print(mamo[1])  # mamo

print('=============================================')
