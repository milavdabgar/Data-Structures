myOddSet = {1, 3, 5, 7, 9}
myEvenSet = {2, 4, 6, 8, 10}

print("My Odd Value Set:")
print(myOddSet)
print("My Even Value Set:")
print(myEvenSet)

myOddSet.add(11)
myEvenSet.add(12)

mySet = myOddSet.union(myEvenSet)
print("Union of Two Sets:")
print(mySet)

mySet = myOddSet.intersection(myEvenSet)
print("Intersection of Two Sets:")
print(mySet)

mySet = myOddSet.difference(myEvenSet)
print("Difference of Two Sets:")
print(mySet)

print("Odd Set and Even Set are disjoint: " +
      str(myOddSet.isdisjoint(myEvenSet)))
print("Odd Set is a subset of Even Set: " + str(myOddSet.issubset(myEvenSet)))
print("Odd Set is a superset of Even Set: " +
      str(myOddSet.issuperset(myEvenSet)))
