# map

print('=============================================')


def fahrenheit(T):
    return (9 / 5) * T + 32


print(fahrenheit(0))  # 32.0

print('=============================================')

temp = [0, 2, 3]

print(list(map(fahrenheit, temp)))  # [32.0, 35.6, 37.4]

print('=============================================')

print(list(map((lambda T: (9 / 5) * T + 32), temp)))  # [32.0, 35.6, 37.4]

print('=============================================')

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

print(list(map((lambda x, y, z: x + y + z), a, b, c)))  # [12, 15, 18]

print('=============================================')
