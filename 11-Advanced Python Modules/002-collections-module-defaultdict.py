# collections module defaultdict
# A defaultdist will never raise a keyError. Any key that does not exist gets the value
# returned by the default factory.

from collections import defaultdict

print('=============================================')

d = {'key1': 'value'}

print(d['key1'])  # value

# print(d['key2'])  # KeyError: 'key2'

print('=============================================')

d2 = defaultdict(object)

print(d2['key1'])  # <object object at 0x7f141bdd80b0>

for item in d2:
    print(item)  # key1

print('=============================================')

d3 = defaultdict(lambda: 0)  # default value is 0 of any key

print(d3['key'])  # 0

d3['key2'] = 5

print(d3['key2'])  # 5

print('=============================================')
