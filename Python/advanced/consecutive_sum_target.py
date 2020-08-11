def sum_pair(l, t):
    l.sort()
    s = 0 # start index
    e = len(l) - 1 # last index

    a, b = 0, 0 # set default return value
    while s < e:
        if (l[s] + l[e] == t):
            a, b = l[s], l[e]
            break
        elif (l[s] + l[e] < t):
            s += 1
        else:
            e -= 1
    return a, b

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


def find_sum(l, t):
    no_pair_sol = (0,0)
    no_seq_sol = [-1, -1]
    check_sum_pair = sum_pair(l, t)
    check_sum_sequence = sum_sequence(l, t)
    if(check_sum_pair != no_pair_sol):
        print('check_sum found: ', check_sum_pair)
    if(check_sum_pair == no_pair_sol):
        print('sum_pair did not find a solution')
    if(check_sum_sequence == no_seq_sol):
        print('sum_sequence did not find a solution')
    if(check_sum_sequence != no_seq_sol):
        print('sum_sequence found: ', check_sum_sequence)


l1 = [4, 3, 5, 7, 8]
target = 12

find_sum(l1, target)
