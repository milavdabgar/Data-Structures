def bubblesort(mylist):
    lenght = len(mylist)
    for i in range(lenght):
        for j in range(lenght-i-1):
            if (mylist[j] > mylist[j+1]):
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp


mylist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("list before sorting:")
print(mylist)
bubblesort(mylist)
print("list after sorting:")
print(mylist)
