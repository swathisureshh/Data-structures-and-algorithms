class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        
    def insertAtBegin(self,newdata):
        if self.head==None:
            newNode=Node(newdata)
            self.head=newNode
        else:
            newNode=Node(newdata)
            newNode.next=self.head
            self.head=newNode
    def display(self):
        if self.head==None:
            print("Empty list")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
                
    def insertAtEnd(self,newdata):
        if self.head==None:
            newNode=Node(newdata)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            newNode=Node(newdata)
            temp.next=newNode
            
    def counting(self):
        count=0
        if self.head==None:
            print(count)
        else:
            temp=self.head
            while temp!=None:
                count+=1
                temp=temp.next
            print(count)
            
    def deleteAtBegin(self):
        if self.head==None:
            return
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            
    def deleteAtEnd(self):
        if self.head==None:
            return
        else:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
            
    # def searchNode(self,target):
    #    if self.head==None:
    #        print('LL empty')
    #    else:
    #        temp=self.head
    #        found=False
    #        while temp!=None:
    #            if temp.data==target:
    #                found=True
    #                break
    #            else:
    #                temp=temp.next
    #        if found!=False:
    #            print('Element Found')
    #        else:
    #             print('Element Not Found')
                   
        def reverse(self):
            if self.head==None:
                print("cant reverse due to empty")
            else:
                prev=None
                temp=self.head
                while temp!=None:
                    nextNode=temp.next
                    temp.next=prev
                    prev=temp
                    temp=nextNode
                self.head=prev
                
        def findMax(self):
            if self.head==None:
                return
            else:
                temp=self.head
                max=self.head.data
                while temp!=None:
                    if temp.data>max:
                        max=temp.data
                    temp=temp.next
                print('Max Ele is:',max)
            
          
             
        
            
                          
obj=SLL()
obj.insertAtBegin(100)
obj.insertAtBegin(200)
obj.insertAtBegin(300)
obj.insertAtBegin(400)
obj.insertAtBegin(500)

obj.insertAtEnd("pallu")
obj.insertAtEnd("Raju")
obj.insertAtEnd("Teju")
obj.counting()

obj.deleteAtBegin()
obj.deleteAtBegin()
obj.deleteAtEnd()
obj.reverse()
obj.findMax()
obj.display()

#obj.searchNode('pallu')