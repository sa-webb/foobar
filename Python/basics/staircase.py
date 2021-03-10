stairs = 6

def staircase(n):
    i = 1
    s = n - 1
    while i <= n:
        print(' ' * s + '#' * i)
        i = i + 1
        s = s - 1
        

staircase(stairs)