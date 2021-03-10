# Compute both the diagonal differences of a square matrix

arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]


def diagonalDifference(arr):
    rows = len(arr)

    s1 = 0
    s2 = 0

    for i in range(0, rows):
        for j in range(0, rows):
            if (i == j):
                s1 = s1 + arr[i][j]
            if (i == rows - j - 1):
                s2 = s2 + arr[i][j]

            
    
    diff = s1 - s2
    return abs(diff)


result = diagonalDifference(arr)
print(result)