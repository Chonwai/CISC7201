import datetime
flag = True
while flag:
    name = input("Give me your name: ")
    age = input("Give me your age: ")
    now = datetime.datetime.now()
    temp = 100 - int(age)
    ans = now.year + temp
    print("100 years old at " + str(ans))
pass
