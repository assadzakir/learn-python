# Tuples
# In Python tuples are very similar to lists, however, unlike lists they are immutable
# meaning they can not be changed. You would use tuples to present things that shouldn't
# be changed, such as days of the week, or dates on a calendar.

#  Constructing Tuples
my_tuples = ('one', 2, 3.99, 4, {'key': 'val'})

#  Basic Tuples Methods
print(len(my_tuples))  # 5

print(my_tuples[4]['key'])  # val

print(my_tuples[-1])  # {'key': 'val'}

print(my_tuples.index({'key': 'val'}))  # 4

print(my_tuples.count('one'))  # 1

#  Immutability
# my_tuples[0] = 'newOne'  # TypeError: 'tuple' object does not support item assignment
