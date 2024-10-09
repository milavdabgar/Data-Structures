class Node:
  def __init__(self, info):
      self.info = info
      self.link = None

class SinglyLinkedList:
  def __init__(self):
      self.FIRST = None
      self.PRED = None
      self.SAVE = None

  def InsertBegining(self, New_Node):
      if self.FIRST is None:
          self.FIRST = New_Node
      else:
          New_Node.link = self.FIRST
          self.FIRST = New_Node

  def display(self):
      if self.FIRST is None:
          print("Linked List is Empty")
      else:
          self.SAVE = self.FIRST
          while self.SAVE is not None:
              if self.SAVE.link is not None:
                  print("{}".format(self.SAVE.info), end="")
              else:
                  print("{}".format(self.SAVE.info))
              self.SAVE = self.SAVE.link


SList = SinglyLinkedList()
while True:
  print("Select Your Option")
  print("(1) Insert New Node At Beginning")
  print("(2) Display Linked List")
  print("(3) EXIT")
  choice = input("Enter Your Choice: ")
  if not choice.isnumeric():
      print("Wrong Choice Entered")
  elif int(choice) == 1:
      Value = input("Enter Element: ")
      New_Node = Node(Value)
      SList.InsertBegining(New_Node)
  elif int(choice) == 2:
      SList.display()
  elif int(choice) == 3:
      break
  else:
      print("Wrong choice Entered")
