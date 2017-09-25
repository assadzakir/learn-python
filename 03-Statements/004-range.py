# range()
# range() Parameters
# range() takes mainly three arguments having the same use in both definitions:

# start - integer starting from which the sequence of integers is to be returned
# stop - integer before which the sequence of integers is to be returned.
# The range of integers end at stop - 1.
# step (Optional) - integer value which determines the increment between each integer in the sequence

print('=============================================')

for el in range(0, 10):
    print(el)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print('=============================================')

for el in range(0, 10, 2):
    print(el)  # 0, 2, 4, 6, 8,

print('=============================================')

print(type(range(7)))  # class range
