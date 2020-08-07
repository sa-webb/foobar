'''
Check if entered word is a palindrome.
'''
w = input("Enter word for palindrome ")

tmp = []
rev_tmp = []
tmp2 = []

for c in w:
    tmp.append(c)

rev_tmp = reversed(tmp)

for i in rev_tmp:
    tmp2.append(i)

if tmp == tmp2:
    print('palindrome')
else:
    print('not a palindrome')

# for x, y in zip(tmp, tmp2):
#     if x == y:
#         continue
#     else:
#         print('Not a palindrome')
#         break
