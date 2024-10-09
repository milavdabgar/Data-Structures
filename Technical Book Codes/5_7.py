def mergesort(mylist1, mylist2, mylist3):
    I = 0
    J = 0
    N1 = len(mylist1)
    N2 = len(mylist2)
    while (I < N1-1 and J <= N2-1):
        if (mylist1[I] < mylist2[J]):
            mylist3.append(mylist1[I])
            I = I+1
        else:
            mylist3.append(mylist2[J])
            J = J+1
    while (I <= N1-1):
        mylist3.append(mylist1[I])
        I = I+1
    while (J <= N2-1):
        mylist2.append(mylist2[J])
        J = J+1


mylist1 = [28, 31, 37, 39]
mylist2 = [24, 35, 43, 53, 85, 89]
mylist3 = []
print("list before sorting: ")
print(mylist1)
print(mylist2)
mergesort(mylist1, mylist2, mylist3)
print("list after sorting: ")
print(mylist3)
