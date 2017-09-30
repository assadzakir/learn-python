# Try, Except Finally

print('=============================================')

# a = 2 + 's'

# print(a)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print('=============================================')

try:
    b = 2 + 's'
except TypeError:
    print('There was a type error!')  # There was a type error!
finally:
    print('Finally This was printed')  # Finally This was printed

print('=============================================')

try:
    c = 2 + 's'
except:
    print('There was a type error!')  # There was a type error!
finally:
    print('Finally This was printed')  # Finally This was printed

print('=============================================')

try:
    f = open('testing', 'w')
    f.write('This is the test file')
except:
    print('Error while opening file')
else:
    print('File write was a successful')  # File write was a successful

print('=============================================')

try:
    f = open('testing2', 'r')
    f.write('This is the test file')
except:
    print('Error while opening file')  # Error while opening file

else:
    print('File write was a successful')

print('=============================================')

try:
    f = open('testing3', 'r')
    f.write('This is the test file')
except:
    print('There was an error')  # There was an error

finally:
    print('Always execute finally code block!')  # Always execute finally code block!

print('=============================================')


def ask_int():
    try:
        val = int(input('Please inter an integer: '))
    except:
        print("looks like you didn't enter integer")
        val = int(input('Try again - Please inter an integer: '))
    finally:
        print('Finally block executed')  # Finally block executed

    print(val)  # user given number



# ask_int()

print('=============================================')


def ask_int2():
    while True:
        try:
            val = int(input('Please inter an integer: '))
        except:
            print("looks like you didn't enter integer")
            continue
        else:
            print("Correct that's an Integer")
            break
        finally:
            print('Finally block executed')  # Finally block executed
        print(val)  # user given number


ask_int2()