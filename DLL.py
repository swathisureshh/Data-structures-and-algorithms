class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertAtBegin(self,newdata):
        if self.head==None or self.tail==None:
            newNode=Node(newdata) 
            self.head=newNode 
            self.tail=newNode 
        else:
            newNode=Node(newdata) 
            newNode.next=self.head
            self.head.previous=newNode
            self.head=newNode
    def insertAtEnd(self,newdata):
         if self.head==None or self.tail==None:
             newNode=Node(newdata)
             self.head=newNode 
             self.tail=newNode 
             
         else:
             temp=self.head
             while temp.next!=None:
                 temp=temp.next
             newNode=Node(newdata)
             temp.next=newNode
             
             
             
    def deleteAtBegin(self):
        if self.head==None:
            return
        else:
            temp=self.head
            self.head=temp.next
        
             
    def deleteAtEnd(self):
        if self.head==None or self.tail==None:
            return
        else:
            temp=self.tail.prev
            self.tail=temp
            temp.next=None
            
             
    def display(self):
        if self.head==None or self.tail==None:
            print('DLl is Empty')
        else:
            temp=self.head
            while temp!=None:
                print(temp.data)
                temp=temp.next
obj=DLL()
obj.insertAtBegin(100)
obj.insertAtBegin(200)
obj.insertAtBegin(300)
obj.insertAtEnd("swathi")
obj.insertAtEnd("anu")
obj.insertAtBegin(400)
obj.insertAtBegin(500)
obj.insertAtEnd("nayi")
obj.deleteAtBegin()
obj.deleteAtEnd()
obj.display()
