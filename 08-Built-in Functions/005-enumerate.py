# enumerate(iterable, start=0)¶

# Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports
# iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from
# start which defaults to 0) and the values obtained from iterating over iterable.

print('=============================================')

l = ['a', 'b', 'c']

index = 0
for item in l:
    print(index)  # 0, 1, 2
    print(item)  # a, b, c
    index += 1

print('=============================================')

for i, item in enumerate(l):
    print(i)  # 0, 1, 2
    print(item)  # a, b, c

print('=============================================')

for i, item in enumerate(l):
    if i >= 2:
        break
    else:
        print(i)  # 0, 1
        print(item)  # a, b

print('=============================================')
