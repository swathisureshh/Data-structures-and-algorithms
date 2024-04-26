class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class QueueLinkedList:
    def _init_(self):
        self.front=None
        self.rear=None
        
    def is_empty(self):
        return self.front is None
    
    def enqueue(self,item):
        new_node=Node(item)
        if self.is_empty():
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
            
    def dequeue(self):
            if not self.is_empty():
                dequeued_item=self.front.data
                self.front=self.front.next
                if self.front is None:
                    self.rear=None
                return dequeuded_item
            else:
                raise IndexError("dequeue from an empty queue")
     def peek(self):
            
            