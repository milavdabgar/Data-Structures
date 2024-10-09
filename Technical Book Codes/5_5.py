def Quicksort(mylist, first, last):
    low = first
    high = last
    pivot = (low+high)//2
    while (low < high):
        while (mylist[low] < mylist[pivot]):
            low = low+1
        while (mylist[high] > mylist[pivot]):
            high = high-1
        if (low <= high):
            temp = mylist[low]
            mylist[low] = mylist[high]
            mylist[high] = temp
            low = low+1
            high = high-1

    print(mylist)
    if (first < high):
        Quicksort(mylist, low, high)
    if (low < last):
        Quicksort(mylist, low, last)


mylist = [43, 3, 20, 89, 4, 77]
print("list before sorting:")
print(mylist)
Quicksort(mylist, 0, len(mylist)-1)
print("list after sorting:")
print(mylist)
