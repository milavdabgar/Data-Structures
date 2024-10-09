import array as arr

A = arr.array('i', [1, 2, 3, 4, 5])

# Insert Element In Array
X = int(input("Enter Value To Insert In Array:"))
A.append(X)

# Insert Element At Specific Position In Array
Index = int(input("Enter Index Position to Where Insert Element:"))
X = int(input("Enter Value To Insert In Array:"))
A.insert(Index, X)

print(A)

# Remove Element From Specific Position
Index = int(input("Enter Index Position From Where To Delete Element:"))
A.pop(Index)

# Remove Specific Element
X = int(input("Enter Element To Delete:"))
A.remove(X)

print(A)
