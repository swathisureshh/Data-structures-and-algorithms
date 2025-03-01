class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, newdata):
        """Insert node at the beginning"""
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self, newdata):
        """Insert node at the end"""
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode  # Fix: Assign head if list is empty
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode

    def display(self):
        """Display the linked list"""
        if self.head is None:
            print("Empty list")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")  # Fix: Print 'None' at the end

    def counting(self):
        """Count the number of nodes"""
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        print(f"Number of nodes: {count}")

    def deleteAtBegin(self):
        """Delete node from the beginning"""
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        self.head = self.head.next  # Fix: Update head to next node

    def deleteAtEnd(self):
        """Delete node from the end"""
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if self.head.next is None:  # Fix: Handle single-node case
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def reverse(self):
        """Reverse the linked list"""
        if self.head is None:
            print("Can't reverse an empty list.")
            return
        prev = None
        current = self.head
        while current is not None:
            nextNode = current.next  # Store next node
            current.next = prev  # Reverse pointer
            prev = current  # Move prev forward
            current = nextNode  # Move current forward
        self.head = prev  # Update head
        print("Linked List reversed successfully!")
        
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

# Example Usage
obj = SLL()
obj.insertAtBegin(100)
obj.insertAtBegin(200)
obj.insertAtBegin(300)
obj.insertAtBegin(400)
obj.insertAtBegin(500)

# obj.insertAtEnd("pallu)
# obj.insertAtEnd('raju)
# obj.insertAtEnd()

print("Original List:")
obj.display()

obj.counting()  # Expected output: 8

obj.deleteAtBegin()
obj.deleteAtBegin()
obj.deleteAtEnd()

print("\nList after deletions:")
obj.display()

obj.reverse()
print("\nReversed List:")
obj.findMax()
obj.display()  # Expected output: pallu -> 100 -> 200 -> None
