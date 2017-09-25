#  For loops

print('=============================================')

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for el in numbers_list:
    print(el)  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print('=============================================')

for el in numbers_list:
    if el % 2 == 0:
        print('even %s' % el)  # 2, 4, 6, 8, 10
    else:
        print('odd %s' % el)  # 1, 3, 5, 7 ,9

print('=============================================')

list_sum = 0

for el in numbers_list:
    list_sum = list_sum + el

print(list_sum)  # 55

print('=============================================')

message = 'Hello Assad'

for letter in message:
    print(letter)  # H, e, l, l, o,  ,A, s, s, a, d

print('=============================================')

my_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for num in my_tup:
    print(num)  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print('=============================================')

list_of_tuples = [(1, 2), (3, 4), (5, 6)]

for tup in list_of_tuples:
    print(tup)  # (1, 2), (3, 4), (5, 6)

print('=============================================')

for (t1, t2) in list_of_tuples:
    print(t1)  # 1 3 5

print('=============================================')

my_dist = {'key1': 'value1', 'key2': 100, 'key3': 99.99}

for item in my_dist:
    print(item)  # key1, key2, key3

print('=============================================')

for (key, value) in my_dist.items():
    print(value)  # value1, 100, 99.99
