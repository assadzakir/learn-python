# Sets
# A set contains an unordered collection of unique and immutable objects.
# The set data type is, as the name implies, a Python implementation
# of the sets as they are known from mathematics.
# This explains, why sets unlike lists or tuples can't have
# multiple occurrences of the same element.

my_set = set()

print(my_set)

my_set.add(1)

print(my_set)  # {1}

my_set.add(2)

print(my_set)  # {1, 2}

my_set.add(2)

print(my_set)  # {1, 2} only unique value

my_list = [1, 1, 1, 2, 3, 4, 4, 4, 5]  # list

print(set(my_list))  # {1, 2, 3, 4, 5} set returns unique elements

# Booleans

my_boolean = True

print(my_boolean)  # True

print(1 > 2)  # False

print(11 > 2)  # True

# None

my_value = None

print(my_value)

my_value = 'val'

print(my_value)
