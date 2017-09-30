# Object Oriented Programming

print('=============================================')


#  Classes
# create a new object type called Sample
class Sample(object):
    pass

# Instance of Sample
x = Sample()

print(type(x))  # <class '__main__.Sample'>

print('=============================================')


# Attributes
# The syntax for creating an attribute is
# self.attribute = something
#
# There is special method called
#
# __init__() This method is used to initialize the attributes of an object.

class Dog(object):

    #  class object attribute
    species = 'mammal'

    def __init__(self, breed, name):  # This method is used to initialize the attributes of an object.
        self.breed = breed
        self.name = name


x = Dog('lap', 'sam')

print(x)  # <__main__.Dog object at 0x7f2f248e9978>
print(x.breed)  # lap
print(x.species)  # mammal
print(x.name)  # sam
