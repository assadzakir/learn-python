# Dictionaries
# A dictionary is an associative array (also known as hashes).
# Any key of the dictionary is associated (or mapped) to a value.
# The values of a dictionary can be any Python data type.
# So dictionaries are unordered key-value-pairs.

#  Constructing a Dictionary
my_dist = {'key1': 'value1', 'key2': 100, 'key3': 99.99}

#  Accessing Objects from a dictionary
print(my_dist['key2'])  # 100

print(my_dist['key1'].upper())  # VALUE1

print(my_dist['key2'] - 2)  # 98

print(my_dist['key2'])  # 100

my_dist['key2'] = my_dist['key2'] - 2

print(my_dist['key2'])  # 98

print(my_dist)  # {'key1': 'value1', 'key2': 98, 'key3': 99.99}

my_colors = {}

my_colors['color1'] = 'red'
my_colors['color2'] = 'green'

print(my_colors)  # {'color1': 'red', 'color2': 'green'}

#  Nesting dictionary
my_dist2 = {'key1': {'subKey': 'value'}, 'key2': 100, 'key3': 99.99}

print(my_dist2['key1']['subKey'].upper())  # VALUE

#  Basic Dictionary Methods

my_dist3 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

print(my_dist3.keys())  # dict_keys(['key1', 'key2', 'key3'])

print(my_dist3.values())  # dict_values(['value1', 'value2', 'value3'])

print(my_dist3.items())  # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

