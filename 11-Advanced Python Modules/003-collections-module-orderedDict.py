# collections module OrderedDict

# An OrderedDict is a dictionary subclass that remembers the order in which its content
# are added
from collections import OrderedDict

print('=============================================')
#  Dictionaries are ordered in Python 3.6+

d = {}

d['e'] = 5
d['d'] = 4
d['c'] = 3
d['b'] = 2
d['a'] = 1

for k, v in d.items():
    print(k, v)

        # e 5
        # d 4
        # c 3
        # b 2
        # a 1
print('=============================================')

d_2 = OrderedDict()

d_2['e'] = 5
d_2['d'] = 4
d_2['c'] = 3
d_2['b'] = 2
d_2['a'] = 1

for k, v in d_2.items():
    print(k, v)

            # e 5
            # d 4
            # c 3
            # b 2
            # a 1
