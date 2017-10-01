# functions within functions

print('=============================================')


def hello(name='Assad'):
    print('The hello function has been executed')

    def greet():
        return '\t This  is inside the greet() function'

    def welcome():
        return '\t This  is inside the welcome() function'

    print(greet())
    print(welcome())
    print('Back to Hello()')


hello()

# The hello function has been executed
# 	 This  is inside the greet() function
# 	 This  is inside the welcome() function
# Back to Hello()


print('=============================================')


def hello_2(name='Assad'):
    def greet():

        return '\t This  is inside the greet() function'

    def welcome():

        return '\t This  is inside the welcome() function'

    if name == 'Assad':
        return greet
    else:
        return welcome


m = hello_2()

print(m())  # This  is inside the greet() function

print('=============================================')
