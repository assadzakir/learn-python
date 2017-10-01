# creating generators

print('=============================================')


def gencubes(n):
    for num in range(n):
        yield num ** 3


for x in gencubes(5):
    print(x)

    # 0
    # 1
    # 8
    # 27
    # 64

print('=============================================')


def genfibon(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


for num in genfibon(5):
    print(num)
    # 1
    # 1
    # 2
    # 3
    # 5

print('=============================================')


def simple_gen():
    for x in range(3):
        yield x


g = simple_gen()

print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
# print(next(g))  # error StopIteration

print('=============================================')

my_string = 'this is string'

for letter in my_string:
    print(letter)  # t h i s  i s  s t r i n g

print('=============================================')

# next(my_string)  # TypeError: 'str' object is not an iterator

print('=============================================')

s = iter(my_string)

print(next(s))  # t
print(next(s))  # h
print(next(s))  # i
print(next(s))  # s

print('=============================================')

