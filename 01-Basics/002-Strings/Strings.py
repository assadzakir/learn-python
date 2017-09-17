_greet = 'Hello'

print(_greet)

_message = 'Hello there'

print(_message)

_message2 = "Hello there"

print(_message2)

_message3 = 'Hello "World"'

print(_message3)

_string1 = 'The standard chunk of Lorem Ipsum used since the 1500s is \n reproduced below for those interested. ' \
           'Sections 1.10.32 and '

print(_string1)

_string2 = 'The standard  \t reproduced'

print(_string2)

# length
print(len(_string2))  # including white spaces _string2 length is 55

# indexing
print(_string2[0])  # T indexing start from 0

print(_string2[1])  # h indexing start from 0

# slicing
print(_string2[1:])  # grab index 1 to onwards

print(_string2[:1])  # T grab up to index 1

print(_string2[:])  # grab everything

print(_string2[-1])  # d grab last one

# reversing string
print(_string2[::-1])

# concatenating
new_sting = _string1 + _string2
print(new_sting)

# upper case
print(_string2.upper())

# lower case
print(_string2.lower())

# split
print(_string2.split())
