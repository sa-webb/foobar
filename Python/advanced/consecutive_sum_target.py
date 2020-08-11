def sum_pair(l, t):
    l.sort()
    s = 0
    e = len(l) - 1
    a, b = 0, 0

    while s < e:
        if (l[s] + l[e] == t):
            a, b = l[s], l[e]
            return a, b
        elif (l[s] + l[e] < t):
            s = + 1
        else:
            e -= 1
        return 0


def sum_sequence(l, t):
    sublist = []
    e = [-1, -1]
    for i in range(len(l)):
        for j in range(i + 1, len(l) + 1):
            target = sum(l[i:j])
            if target == t:
                sublist.append(i)
                sublist.append(j - 1)
                return sublist
    return e


def main(l,t):
    check_sum_pair = sum_pair(l,t)
    check_sum_sequence = sum_sequence(l,t)
    if(check_sum_pair == 0):
        print('There was not a pair of numbers that hit the target')
    elif(check_sum_sequence == [-1,-1]):
        print('There was not a sequence of numbers that hit the target')
    else:
        pass


l1 = [4, 3, 5, 7, 8]
target = 7

print(sum_pair(l1, target))
# print(main(l1, target))