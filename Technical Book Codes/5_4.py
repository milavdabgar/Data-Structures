def SelectionSort(myList):
    K = 1
    Length = len(myList)
    for I in range(Length):
        MIN = myList[I]
        POS = I

        for J in range(I+1, Length):
            if (myList[J] < MIN):

                MIN = myList[J]
                POS = J

            temp = myList[I]
            myList[I] = myList[POS]
            myList[POS] = temp
            print("PASS {}:{}".format(K, myList))
            K = K+1


myList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("List Before Sorting:")
print(myList)
SelectionSort(myList)
print("list after sorting:")
print(myList)
