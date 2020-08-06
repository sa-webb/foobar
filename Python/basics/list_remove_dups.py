'''
Function takes any list as a parameter.
Create a new list that will not contain the duplicates.
For all elements in the passed list, if that element does not exist in the new
list, then add it to the new list.
'''


def rm_duplicates(l):
    temp_list = []
    for i in l:
        if i not in temp_list:
            temp_list.append(i)
    return temp_list


a = [1, 2, 3, 4, 3, 2, 1]
print(rm_duplicates(a))
