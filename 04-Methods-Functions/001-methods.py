#  Methods
#  The other kind of instance attribute reference is a method.
#  A method is a function that “belongs to” an object.
# (In Python, the term method is not unique to class instances:
# other object types can have methods as well.
# For example, list objects have methods called append, insert, remove, sort, and so on.

print('=============================================')

my_list = [1, 2, 3]

my_list.append(4)

print(my_list)  # [1, 2, 3, 4]

print('=============================================')

print(my_list.count(3))  # 1

print('=============================================')

print(help(my_list.append))  # append(...) method of builtins.list instance

print('=============================================')
