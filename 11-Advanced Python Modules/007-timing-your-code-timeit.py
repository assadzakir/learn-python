# Timing code
print('=============================================')

import timeit

string1 = '-'.join(str(n) for n in range(100))

print(string1)  # 0-1-2-3-4-5-6-7-8-9-10-11-12-13 .... -99

print('=============================================')

timing1 = timeit.timeit(str(string1), number=10000)

print(timing1)  # 0.04265698000017437

print('=============================================')

string2 = '-'.join([str(n) for n in range(100)])

timing2 = timeit.timeit(str(string2), number=10000)

print(timing2)  # 0.03608939100013231

print('=============================================')

timing3 = timeit.timeit('-'.join(map(str, range(100))), number=10000)

print(timing3)  # 0.03912280999975337