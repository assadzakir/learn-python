# string
print('Hello world')

# string (you can use the %s to format strings into your print statements)
x = 'Assad'

print('Place my var here %s ' % x)

x = 0000

print('Place my var here %s ' % x)

x = 10.11

print('Floating point number %s ' % x)

# Floating point Number (you can use the %n1:n2f to format floating point Number into your print statements)
f = 10.11

print('Floating point number %1.3f ' % f)

f = 10.11

print('Floating point number %12.3f ' % f)

# conversion format methods
num = 123

print('Convert to string %r' % num)

num = 123

print('Convert to string %s' % num)

# Multiple Formatting
print('First: %s, Second: %s, Third: %s' % ('baz', 'bar', 'boo'))

# using the string.format() method
print('First: {x} Second: {y} Third: {z}'.format(x=1, y=2, z=3))
