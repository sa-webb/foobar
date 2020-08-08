# Find the overlapping contents of the files

file_contents1 = []
file_contents2 = []
overlap = []

with open('./nums1.txt', 'r') as nums1_file:
    for line in nums1_file:
        file_contents1.append(int(line))

with open('./nums2.txt', 'r') as nums2_file:
    for line in nums2_file:
        file_contents2.append(int(line))


for i in file_contents1:
    if i in file_contents2:
        overlap.append(i)


print('Overlapping elements: ', overlap)
