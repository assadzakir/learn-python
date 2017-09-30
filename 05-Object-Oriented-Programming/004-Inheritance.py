# Object Oriented Programming

print('=============================================')


#  Inheritance

class Animal(object):
    def __init__(self):
        print('Animal Created')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')


a = Animal()

print(a)  # Animal Created

print('=============================================')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    def whoAmI(self):
        print('Dog')

    def bark(self):
        print('Woof!')


d = Dog()
print(d)  # Animal Created,  Dog Created
print(d.whoAmI())  # Dog
print(d.eat())  # Eating
print(d.bark())  # Woof!
