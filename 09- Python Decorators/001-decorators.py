# decorators

print('=============================================')


def func():
    return 1


print(func())  # 1

print('=============================================')

s = 'this is string'


def func_2():
    return locals()


print(func_2())  # {}
print(globals()['s'])  # this is string

print('=============================================')


def hello(name='Assad'):
    return 'Hello ' + name


print(hello())  # Hello Assad

message = hello

print(message())  # Hello Assad

del hello

# print(hello())  #  NameError: name 'hello' is not defined


print(message())  # Hello Assad

print('=============================================')
