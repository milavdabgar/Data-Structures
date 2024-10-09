class stack:
    def __init__(self):
        self.element = []
        self.maxsize = 10
        self.top = -1

    def Push(self, Value):
        if (self.top >= self.maxsize-1):
            print("Stack Is Overflow")
            return
        self.top = self. top+1
        self.element.append(Value)

    def size(self):
        return len(self.element)

    def topofstack(self):
        if (self.top == -1):
            print('Stack is Underflow')

        else:
            print("TOP ElementIs: {}".format(self.element[self.top]))

    def Pop(self):
        if (self.top == -1):
            print('Stack Is Underflow')
            return
        print("deleted element Is:{}".format(self.element.pop()))
        self.top = self.top-1

    def display(self):
        if (self.top == -1):
            print("Stack Is Underflow")
        else:
            print("Elements in the stack are:")
            for i in range(self.top, -1, -1):
                print(self.element[i])


s = stack()
while (True):

    print("Select Your Option")
    print("(1) PUSH Element")
    print("(2) POP Element")
    print("(3) Display Element of Stack")
    print("(4) Display TOPMOST Element of Stack")
    print("(5) Size of Stack")
    print("(6) EXIT")
    choice = input("Enter Your Choice: ")
    if (choice.isnumeric() is False):
        print("Wrong Choice Entered")
    elif (int(choice) == 1):
        Value = input("Enter Element:")
        s. Push(Value)
    elif (int(choice) == 2):
        s. Pop()
    elif (int(choice) == 3):
        s.display()
    elif (int(choice) == 4):
        s.topofstack()
    elif (int(choice) == 5):
        print("Size of Stack Is: {}".format(s.size()))
    elif (int(choice) == 6):
        break
    else:
        print("wrong choise entered")
