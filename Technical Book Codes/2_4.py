class Company:
    def __init__(self, CompanyName):
        self.CompanyName = CompanyName

    def DisplayCompany(self):
        print("Company Name:", self.CompanyName)


class Purchase(Company):
    def __init__(self, CompanyName, ManagerName):
        super().__init__(CompanyName)
        self.ManagerName = ManagerName

    def DisplayPurchase(self):
        self.DisplayCompany()
        print("Manager Name:", self.ManagerName)


class Sales(Company):
    def __init__(self, CompanyName, ManagerName):
        super().__init__(CompanyName)
        self.ManagerName = ManagerName

    def DisplaySales(self):
        self.DisplayCompany()
        print("Manager Name:", self.ManagerName)


CompanyName = input("Enter Company Name:")
PurchaseManagerName = input("Enter Purchase Manager Name:")
SalesManagerName = input("Enter Sales Manager Name:")

P = Purchase(CompanyName, PurchaseManagerName)
P.DisplayPurchase()

S = Sales(CompanyName, SalesManagerName)
S.DisplaySales()
