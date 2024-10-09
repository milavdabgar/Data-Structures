Student = {"Name": "Yesha", "RollNumber": 13, "Standard": 10}

print(Student)

Student.update({"Division": "C"})

if "Name" in Student:
    print("Name Key Exists in Student")
else:
    print("Name Key Does Not Exist in Student")

if "Yesha" in Student.values():
    print("Yes")
else:
    print("No")

for x in Student.items():
    print(x)
