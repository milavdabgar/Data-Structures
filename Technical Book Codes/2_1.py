class Employee:
    def Displayinfo(self):
        print("Name: {}".format(self.Name))
        print("Designation: {}".format(self.Designation))

    def Getinfo(self):
        self.Name = input("Enter Name: ")
        self.Designation = input("Enter Designation: ")


E = Employee()
E.Getinfo()
E.Displayinfo()
