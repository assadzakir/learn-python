# chained comparison operators

print(1 > 2 > 3)  # False

print(1 > 2 and 2 > 3)  # False

print(1 < 3 > 2)  # True

print(1 < 3 and 3 > 2)  # True

print(1 > 3 or 3 > 2)  # True

print(1 == 1 or 3 > 100)  # True
