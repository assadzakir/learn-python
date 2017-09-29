# Functions
# A function is a block of organized, reusable code that is
# used to perform a single, related action.
# Functions provide better modularity for your application and a
# high degree of code reusing.
# As you already know, Python gives you many built-in functions like print(), etc.
# but you can also create your own functions.

print('=============================================')


def add_func(n1, n2):
    return n1 + n2


print(add_func(9, 9))

print('=============================================')


def add_func2(n1, n2):
    """
    doc string hint
    """
    return n1 + n2


print(help(add_func2))  # doc string hint

print('=============================================')


def my_greeting(name):
    print("Hello " + name)


my_greeting('Assad')  # Hello Assad

print('=============================================')


def is_prime(num):
    """
    INPUT: A number
    OUTPUT: A print statement whether or not the number is prime.
    """
    for n in range(2, num):
        if num % n == 0:
            print('Not Prime')
            break
    else:
        print('The number is Prime!')


is_prime(12)  # Not Prime

print('=============================================')
