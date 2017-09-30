# Errors and Exceptions

# In Python, there are two kinds of errors: syntax errors and exceptions.

# Syntax Errors
# Let's start with syntax errors, (also known as parsing errors).

# The parser repeats the offending line and displays an 'arrow' pointing at the
# earliest point in the line where the error was detected.
#
# The error is caused by (or at least detected at) the token preceding the arrow:
# in the  example, the error is detected at the keyword print, since a colon (':')
# is missing before it.
#
# File name and line number are printed so you know where to look in case the
# input came from a script.

# Example of a syntax error
#
# >>> while True print 'Hello world'
#   File "", line 1, in ?
#     while True print 'Hello world'
#                    ^
# SyntaxError: invalid syntax



# Exceptions
# The other kind of errors in Python are exceptions.
#
# Even if a statement or expression is syntactically correct, it may cause an
# error when an attempt is made to execute it.
#
# Errors detected during execution are called exceptions.
#
# Exceptions come in different types, and the type is printed as part of the
# message
#
# The types in the example are ZeroDivisionError, NameError and TypeError.


# Example of an exception error.
# >>> 10 * (1/0)
# Traceback (most recent call last):
#   File "", line 1, in ?
# ZeroDivisionError: integer division or modulo by zero
# >>> 4 + spam*3
# Traceback (most recent call last):
#   File "", line 1, in ?
# NameError: name 'spam' is not defined
# >>> '2' + 2
# Traceback (most recent call last):
#   File "", line 1, in ?
# TypeError: cannot concatenate 'str' and 'int' objects
