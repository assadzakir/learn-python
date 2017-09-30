# Object Oriented Programming
# Everything in Python is an object, and almost everything has attributes and methods.
# All functions have a built-in attribute __doc__, which returns the doc string defined in the function's source
# code. The sys module is an object which has (among other things) an attribute called path. And so forth.
#
#
#  Objects

print('=============================================')

l = [1, 2, 3]

print(type(l))  # It's a list object

print('=============================================')

print(type(1))  # It's a int object

print('=============================================')

print(type((1, 5)))  # It's a tuple object

print('=============================================')

print(type({'key': 'value'}))  # It's a dict object

print('=============================================')


def square(num): return num ** 2


print(type(square))  # It's a function object


#  we can create our own object type using class keyword
