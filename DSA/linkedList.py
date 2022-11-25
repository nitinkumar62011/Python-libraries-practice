class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertionAtBegining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def printLinkedList(self):
        temp=self.head
        print("Element are -----")
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.next
    def insertedAtEnd(self,data):
        temp=self.head
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
    def deleteAtPosition(self,position):
        if self.head is None:
            return
        if position==0:
            self.head=self.head.next
            return
        temp=self.head
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        if temp.next is None:
            return
        if temp is None:
            return
        temp.next=temp.next.next
    def search(self,key):
        temp=self.head
        while temp is not None:
            if key==temp.data:
                return True
            temp=temp.next
        return False


        
list=LinkedList()
# list.insertionAtBegining(9)
# list.insertionAtBegining(10)
list.insertedAtEnd(45)
list.insertedAtEnd(450)
list.insertedAtEnd(451)
list.insertedAtEnd(431)
list.insertedAtEnd(51)
list.insertedAtEnd(651)
list.deleteAtPosition(2)
list.printLinkedList()
if list.search(40)==True:
    print("Element is Found")
else:
    print('Element is not found')