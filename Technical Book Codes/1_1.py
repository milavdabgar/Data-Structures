fruit = ["Apple", "Banana", "Grapes", "Watermelon"]

# Sort the list
fruit.sort()

# Reverse the list
fruit.reverse()

print("Number of Fruits in the List are: " + str(len(fruit)))

i = 0

print(fruit)

fruit.insert(1, "Guava")
fruit.remove("Banana")

print(fruit)

print("Individual Fruits:")
while i < len(fruit):
    print(fruit[i])
    i = i + 1

print("Sorted List:")
print(fruit)

print("Reverse List:")
fruit.reverse()
print(fruit)
