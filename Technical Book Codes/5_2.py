def binarysearch(mylist, x):
    low = 0
    high = len(mylist)-1
    while (low <= high):
        middle = (low+high)//2
        if (x < mylist[middle]):
            high = middle-1
        elif (x > mylist[middle]):
            low = middle + 1
        else:
            return middle
    return None


mylist = [11, 22, 33, 44, 55]
print(mylist)
x = int(input("enter value to search:"))
result = binarysearch(mylist, x)
if (result == None):
    print("search is unsucceccful")
else:
    print("{} is found at position {}".format(x, result))
