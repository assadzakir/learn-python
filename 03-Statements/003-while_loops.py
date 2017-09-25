# while loops
# Using else Statement with Loops

# Python supports to have an else statement associated with a loop statement.

# If the else statement is used with a for loop,
# the else statement is executed when the loop has exhausted iterating the list.

# If the else statement is used with a while loop,
# the else statement is executed when the condition becomes false.

print('=============================================')

num = 0
while num < 10:
    print(num)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    num += 1

print('=============================================')

num2 = 0

while num2 < 10:
    print(num2)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    num2 += 1
else:
    print('Done')  # Done

print('=============================================')

# Break Continue Pass
x = 0

while x < 10:
    print(x)
    x += 1

    if x == 3:
        print('x is 3')
    else:
        print('continuing....')
        continue

print('=============================================')

z = 0

while z < 10:
    print(z)
    z += 1

    if z == 3:
        print('z is 3')
        break
    else:
        print('continuing....')
        continue
