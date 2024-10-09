class GrandFather:
    def __init__(self, GrandFatherName):
        self.GrandFatherName = GrandFatherName


class Father(GrandFather):
    def __init__(self, GrandFatherName, FatherName):
        super().__init__(GrandFatherName)
        self.FatherName = FatherName


class Son(Father):
    def __init__(self, GrandFatherName, FatherName, SonName):
        super().__init__(GrandFatherName, FatherName)
        self.SonName = SonName

    def DisplayFullName(self):
        print("My Name Is: {}".format(self.SonName))
        print("My Father Name Is: {}".format(self.FatherName))


GrandFatherName = input("Enter Grandfather Name: ")
FatherName = input("Enter Father Name: ")
SonName = input("Enter Son Name: ")

son_instance = Son(GrandFatherName, FatherName, SonName)
son_instance.DisplayFullName()
