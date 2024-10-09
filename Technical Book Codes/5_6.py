def insertionsort(mylist):
    k = 1
    lenght = len(mylist)
    for i in range(lenght):
        key = mylist[i]
        for j in range(i, 0, -1):
            if (key < mylist[j-1]):
                temp = mylist[j]
                mylist[j] = mylist[j-1]
                mylist[j-1] = temp
                print("pass {}:{}".format(k, mylist))
                k = k+1


mylist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("list before sorting:")
print(mylist)
insertionsort(mylist)
print("list after sorting:")
print(mylist)
