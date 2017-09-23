# creating lists
my_list = ['assad', 'jawad', 'zubair']

print(my_list)

my_list = ['assad', 100, 55.30, 'zubair']

print(my_list)

print(len(my_list))

# indexing and slicing lists
numbers = [1, 2, 3, 4, 5, 6]

print(numbers[1])  # 2

print(numbers[1:])  # 2, 3, 4, 5, 6

print(numbers[:3])  # 1, 2, 3

print(numbers + [7])  # concatenating 1, 2, 3, 4, 5, 6, 7

print(numbers)  # 1, 2, 3, 4, 5, 6

numbers = numbers + [7]

print(numbers)  # 1, 2, 3, 4, 5, 6,7

# basic list methods
num = [100, 200, 300]

num.append(400)

print(num)  # 100, 200, 300, 400

print(num.pop())  # 400

print(num.pop(0))  # 100

# print(num[2])  # IndexError: list index out of range

colors_list = ['green', 'white', 'blue', 'orange', 'pink']

colors_list.reverse()

print(colors_list)  # 'pink', 'orange', 'blue', 'white', 'green'

colors_list.sort()

print(colors_list)  # 'blue', 'green', 'orange', 'pink', 'white'

# nested lists
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

matrix = [list_1, list_2, list_3]

print(matrix[0])  # 1, 2, 3

print(matrix[0][0])  # 1


# Introduction to list comprehensions
first_col = [row[0] for row in matrix]

print(first_col)  # [1, 4, 7]
