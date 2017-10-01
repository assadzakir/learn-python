# Note: this assumes Python 3.x syntax.†
#
# A generator is simply a function which returns an object on which you can call next, such that for every call it
# returns some value, until it raises a StopIteration exception, signaling that all values have been generated. Such
# an object is called an iterator.
#
# Normal functions return a single value using return, just like in Java. In Python, however, there is an
# alternative, called yield. Using yield anywhere in a function makes it a generator. Observe this code:
