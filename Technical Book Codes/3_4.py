def FIBO(number):
    if (number == 0 or number == 1):
        return 0
    elif (number == 2):
        return 1
    else:
        return (FIBO(number-1)+FIBO(number-2))


number = int(input("enter number:"))
print("FIBO={}".format(FIBO(number)))
