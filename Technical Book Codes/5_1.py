def linearsearch(mylist, x):
    lenght = len(mylist)
    for i in range(lenght):
        if (mylist[i] == x):
            return i
    return None


mylist = [11, 44, 55, 33, 22]
print(mylist)
x = int(input("enter value to search:"))
result = linearsearch(mylist, x)
if (result == None):
    print("search  is unsuccessful")
else:
    print("{} is found at position {}".format(x, result))
