def RemoveDuplicate(MainList):
    Length = len(MainList)
    WithoutDuplicate = []

    for i in range(Length):
        if MainList[i] not in WithoutDuplicate:
            WithoutDuplicate.append(MainList[i])

    return WithoutDuplicate


MainList = []

Value = int(input("How Many Elements In List? "))

for i in range(Value):
    X = int(input("Enter Value: "))
    MainList.append(X)

print("Main List:", MainList)
print("List After Removing Duplicate:", RemoveDuplicate(MainList))
