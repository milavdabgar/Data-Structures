def gcd(n1, n2):
    r = n1 % n2
    if (r == 0):
        return n2
    else:
        return (gcd(n2, r))


n1 = int(input("enter number:"))
n2 = int(input("enter number:"))
print("gcd({},{})={}".format(n1, n2, gcd(n1, n2)))
