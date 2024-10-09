class Student:
    def __init__(self, RollNumber, Name):
        self.RollNumber = RollNumber
        self.Name = Name

    def DisplayStudent(self):
        print("Roll Number: {}".format(self.RollNumber))
        print("Name: {}".format(self.Name))


class Exam:
    def __init__(self, Mark1, Mark2, Mark3):
        self.Mark1 = Mark1
        self.Mark2 = Mark2
        self.Mark3 = Mark3

    def DisplayMark(self):
        print("Mark1: {}".format(self.Mark1))
        print("Mark2: {}".format(self.Mark2))
        print("Mark3: {}".format(self.Mark3))


class Result(Student, Exam):
    def __init__(self, RollNumber, Name, Mark1, Mark2, Mark3):
        Student.__init__(self, RollNumber, Name)
        Exam.__init__(self, Mark1, Mark2, Mark3)

    def DisplayResult(self):
        self.Total = self.Mark1 + self.Mark2 + self.Mark3
        self.Percentage = (self.Total * 100) / 210
        self.DisplayStudent()
        self.DisplayMark()
        print("Total Mark: {}".format(self.Total))
        print("Percentage: {}".format(self.Percentage))


RollNumber = int(input("Enter Roll Number:"))
Name = input("Enter Name:")
Mark1 = int(input("Enter Mark1:"))
Mark2 = int(input("Enter Mark2:"))
Mark3 = int(input("Enter Mark3:"))

R = Result(RollNumber, Name, Mark1, Mark2, Mark3)
R.DisplayResult()
