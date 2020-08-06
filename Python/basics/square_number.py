import sys

for line in sys.stdin:
    print(line)
    num = int(line)
    squared = num * num
    print('squared: ', squared)