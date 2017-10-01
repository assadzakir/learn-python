# functions as Arguments

print('=============================================')


def hello():
    return 'Hello'


def other_fun(fun):
    print('other fun')
    print(fun())


other_fun(hello)  # other fun , Hello

print('=============================================')


def new_decorator(func):
    def wrap_func():
        print('code here, before executing the func')

        func()

        print('code here will execute after the func()')

    return wrap_func


def func_needs_decorator():
    print('This function needs a decorator !')


func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()

# code here, before executing the func
# This function needs a decorator !
# code here will execute after the func()

print('=============================================')


@new_decorator
def func_needs_decorator_2():
    print('This function needs a decorator !')


func_needs_decorator_2()

# code here, before executing the func
# This function needs a decorator !
# code here will execute after the func()

print('=============================================')
