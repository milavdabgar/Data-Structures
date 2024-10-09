class Student:
    def __init__(self, RollNumber, Name):
        self.RollNumber = RollNumber
        self.Name = Name

    def DisplayStudent(self):
        print("Roll Number: {}".format(self.RollNumber))
        print("Name: {}".format(self.Name))


class Result(Student):
    def __init__(self, RollNumber, Name, Marks):
        Student.__init__(self, RollNumber, Name)
        self.Marks = Marks

    def Display(self):
        Student.DisplayStudent(self)
        print("Total Marks: {}".format(self.Marks))


RollNumber = int(input("Enter Roll Number:"))
Name = input("Enter Name:")
TotalMarks = int(input("Enter Total Marks:"))

R = Result(RollNumber, Name, TotalMarks)

R.Display()
