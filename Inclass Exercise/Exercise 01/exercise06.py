text = input("Input the string: ")
check = 0
lastPosition = int(len(text) - 1)
for i in range(0, int(len(text) / 2)):
    if text[i] == text[lastPosition - i]:
        check = check + 1
        pass
    pass
if check == len(text) / 2:
    print("The string is palindrome!")
else:
    print("The string is not palindrome!")
    pass
