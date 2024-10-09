class Node:
    def __init__(self, info):
        self.lptr = None
        self.rptr = None
        self.info = info

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

    def Preorder(self, root):
        if root is not None:
            print(root.info)
            if root.lptr is not None:
                self.Preorder(root.lptr)
            if root.rptr is not None:
                self.Preorder(root.rptr)


root = Node(5)
root.insert(3)
root.insert(8)
root.insert(1)
root.insert(4)
root.insert(7)
root.insert(10)

root.Preorder(root)
