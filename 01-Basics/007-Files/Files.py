# Files
#  When you're working with Python, you don't need to
# import a library in order to read and write files. ...
# When you use the open function, it returns something called a
#  file object. File objects contain methods and attributes that can
# be used to collect information about the file you opened.

file = open('some-text')

print(file.read())  # Hey Assad how are you ? Hey Jawad how are you ?

print(file.read())  #

file.seek(0)  #

print(file.read())  # Hey Assad how are you ? Hey Jawad how are you ?

file.seek(0)

print(file.readlines())  # ['Hey Assad how are you ?\n', 'Hey Jawad how are you ?']

print('=============================================================================')
for line in open('some-text'):
    print(line)