Number = int(input("Enter Number of Element: "))
myNumberList = list()

NegNum = 0
PosNum = 0
ZeroNum = 0
OddNum = 0
EvenNum = 0
Sum = 0

for i in range(1, Number+1):
    N = int(input("Enter Value: "))
    myNumberList.append(N)

    if N < 0:
        NegNum += 1
    elif N > 0:
        PosNum += 1
    else:
        ZeroNum += 1

    if N % 2 == 0:
        EvenNum += 1
    else:
        OddNum += 1

    Sum += N

Average = Sum / Number

print(myNumberList)
print("Number of Positive Numbers: " + str(PosNum))
print("Number of Negative Numbers: " + str(NegNum))
print("Number of Zero Numbers: " + str(ZeroNum))
print("Number of Odd Numbers: " + str(OddNum))
print("Number of Even Numbers: " + str(EvenNum))
print("Average of All Numbers: " + str(Average))
