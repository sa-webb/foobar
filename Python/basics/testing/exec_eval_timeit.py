from eval1 import a
from eval2 import b

import timeit

print(timeit.timeit(a, number=1))
print(timeit.timeit(b, number=1))