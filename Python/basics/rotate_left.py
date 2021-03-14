# Example array: [1,2,3,4,5]
# Rotate 1 = [2, 3, 4, 5, 1]
# Rotate 2 = [3, 4, 5, 1, 2]
# Rotate 3 = [4, 5, 1, 2, 3]
# Rotate 4 = [5, 1, 2, 3, 4]

# n Rotations
d = 1
a = [1,2,3,4,5]
def rotLeft(a,d):
    l = len(a)
    rev = []
    for i in range(d, l):
        rev.append(a[i])
    for j in range(0, d):
        rev.append(a[j])
    print(rev)

rotLeft(a,d)
