# Object Oriented Programming

print('=============================================')


#  Methods

# create a new object type called Circle
class Circle(object):
    #  class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        # radius **2 * pi
        return (self.radius ** 2) * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_radius(self):
        return self.radius


c = Circle(5)

print(c.pi)  # 3.14
print(c.radius)  # 1
print(c.area())  # 78.5
c.set_radius(100)
print(c.radius)  # 100
print(c.get_radius())  # 100

print('=============================================')
