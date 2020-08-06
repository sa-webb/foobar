# Reverse a sentence from input

def reversed(sentence):
    temp = sentence.split()  # Put into array
    temp.reverse()
    return " ".join(temp)


test = input('Enter sentence')
print(reversed(test))
