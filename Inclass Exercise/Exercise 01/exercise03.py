a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lessList = []
biggerList = []
for i in a:
    if i < 5:
        lessList.append(i)
    elif i > 5:
        biggerList.append(i)
    pass
print(lessList)
print(biggerList)
