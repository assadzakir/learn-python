# filter

print('=============================================')

l = range(11)


def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(check_even(34))  # True

print('=============================================')

print(list(filter(check_even, l)))  # [0, 2, 4, 6, 8, 10]

print('=============================================')

print(list(filter((lambda num: num % 2 == 0), l)))  # [0, 2, 4, 6, 8, 10]

print('=============================================')

print(list(filter((lambda num: num > 5), l)))  # [6, 7, 8, 9, 10]
