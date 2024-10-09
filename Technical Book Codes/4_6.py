class Node:
  def __init__(self,info):
      self.info=info
      self.link=None

class SinglyLinkedList:
  def __init__ (self):
      self.FIRST=None
      self.PRED=None
      self.SAVE=None

  def InsertEnd (self, New_Node):
      if (self.FIRST is None):
          self.FIRST=New_Node
      else:
          self.SAVE=self.FIRST
          while (self.SAVE.link is not None):
              self.SAVE=self.SAVE.link
          self.SAVE.link=New_Node

  def DeleteFirst(self):
      if (self.FIRST is None): 
          print ("Linked List is Empty")
      elif(self.FIRST.link is None):
          print ("Deleted Element is (}".format(self.FIRST.info))
          self.FIRST=None
      else:
          print ("Deleted Element is {}".format(self.FIRST.info)) 
          self.FIRST=self.FIRST.link

  def display(self):
      if (self.FIRST is None):
          print("Linked List is Empty")
      else:
          self.SAVE=self.FIRST
          while (self.SAVE is not None):  
              if (self.SAVE.link is not None):
                  print("{}".format(self.SAVE.info), end="")
              else:
                  print("{}".format(self.SAVE.info)) 
              self.SAVE=self.SAVE.link

SList = SinglyLinkedList()
while (True):
  print ("Select Your Option")
  print("(1) Insert New Node At End")
  print(" (2) Delete First Node")
  print("(3) Display Linked List")
  print("(4) EXIT")
  choice = input ("Enter Your Choice: ")
  if (choice.isnumeric() is False):
      print("Wrong Choice Entered")
  elif (int(choice) ==1):
      Value = input("Enter Element:")
      New_Node = Node(Value)
      SList.InsertEnd(New_Node)
  elif (int(choice) ==2):
      SList.DeleteFirst()
  elif (int(choice) ==3):
      SList.display()
  elif(int(choice) ==4):
      break
  else:
      print("Wrong Choice Entered")
