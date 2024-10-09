def factorial(number):
    if (number == 1):
        return 1
    else:
        return number*(factorial(number-1))


number = int(input("enter a number:"))
print("factorial of {} is {}".format(number, factorial(number)))
