a = [1, 2, 3, 4]
b = [2, 4, 5]

def list_intersection(a, b):
    result = list(set(a).intersection(set(b)))
    print(result)

list_intersection(a,b)