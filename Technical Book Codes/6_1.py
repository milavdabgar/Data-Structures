class Node:
    def __init__(self, info):
        self.info = info
        self.lptr = None
        self.rptr = None

    def insert(self, info):
        if info < self.info:
            if self.lptr is None:
                self.lptr = Node(info)
            else:
                self.lptr.insert(info)
        elif info > self.info:
            if self.rptr is None:
                self.rptr = Node(info)
            else:
                self.rptr.insert(info)

    def display(self):
        if self:
            if self.lptr:
                self.lptr.display()
            print(self.info)
            if self.rptr:
                self.rptr.display()


root = Node(5)
root.insert(3)
root.insert(8)
root.insert(1)
root.insert(4)
root.insert(7)
root.insert(10)
root.display()
