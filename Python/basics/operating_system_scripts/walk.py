import os

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)
    for subs in dirs:
        print(subs)