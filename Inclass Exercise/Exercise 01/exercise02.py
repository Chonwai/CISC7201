num = input("Give me a number: ")
if int(num) % 4 == 0:
    print("It can divided by 4")
else:
    if int(num) % 2 == 0:
        print("It is even number!")
    elif int(num) % 2 == 1:
        print("It is odd number!")
        pass
    pass
