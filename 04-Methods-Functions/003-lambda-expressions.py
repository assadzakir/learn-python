# Lambda Expressions

print('=============================================')


def square(num): return num ** 2


print(square(4))  # 16

print('=============================================')

square_2 = lambda num: num ** 2

print(square_2(4))  # 16

print('=============================================')

is_even = lambda num: num % 2 == 0

print(is_even(4))  # True
print(is_even(3))  # False

print('=============================================')

my_reverse = lambda s: s[::-1]

print(my_reverse('Assad'))  # dassA
print(my_reverse('Jawad'))  # dawaJ

print('=============================================')

add_fun = lambda x, y: x + y

print(add_fun(5, 5))  # 10
print(add_fun(9, 9))  # 18
