# class complex([real[, imag]]

# Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the
# first parameter is a string, it will be interpreted as a complex number and the function must be called without a
# second parameter. The second parameter can never be a string. Each argument may be any numeric type (including
# complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and
# float. If both arguments are omitted, returns 0j.

print('=============================================')

print(complex(2, 3))  # (2+3j)

print(complex(10, 1))  # (10+1j)

print(complex('10+2j'))  # (10+2j)

# Note
# When converting from a string, the string must not contain whitespace around the central + or - operator. For
# example, complex('1+2j') is fine, but complex('1 + 2j') raises ValueError.