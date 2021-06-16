def palindrome(input_string):
    lowercase = input_string.lower()
    splitt = lowercase.strip()
    repl = splitt.replace(" ", "")

    forward = ""
    backward = ""
 
    for char in repl:
        forward = forward + char
        backward = char + backward

    if forward == backward:
        return True
    return False

print(palindrome("HannaH HannAH")) # True
print(palindrome("aldjkfh")) # False
print(palindrome("radar")) # True