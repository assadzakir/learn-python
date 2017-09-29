# Nested Statements and Scope

# Actually, a concise rule for Python Scope resolution, from Learning Python, 3rd. Ed..
# (These rules are specific to variable names, not attributes.
# If you reference it without a period, these rules apply)

# LEGB Rule.

# L, Local — Names assigned in any way within a function (def or lambda)), and not declared global in that function.

# E, Enclosing-function locals — Name in the local scope of any and all statically enclosing functions (def or
# lambda), from inner to outer.

# G, Global (module) — Names assigned at the top-level of a module file, or by executing a global statement in a
# def within the file.

# B, Built-in (Python) — Names preassigned in the built-in names module : open,range,SyntaxError,...

print('=============================================')

# Local
# x is local here
a = lambda x: x ** 2

print('=============================================')

# Enclosing function locals
name = 'This is a global name'


def greet():
    # Enclosing function
    name = 'Assad'

    def hello():
        print('Hello ' + name)

    hello()


print(greet())  # Hello Assad

print('=============================================')

# Global
print(name)  # This is a global name

print('=============================================')

# Built-in
print(len)  # <built-in function len> This is a built- in

print('=============================================')

# Local Variables

num = 50


def func():
    num = 10
    print('changed local num to ', num)  # changed local num to  10


func()
print('num is still ', num)  # num is still  50

print('=============================================')

# Global Statement
num_2 = 50


def func_2():
    global num_2
    print('global num_2 is ', num_2)  # global num_2 is  50
    num_2 = 10
    print('changed local num_2 to ', num_2)  # changed local num_2 to  10


func_2()
print('now num_2 is changed at global level due to global statement', num_2)  # now num_2 is changed at global level
# due to global statement 10

print('=============================================')
