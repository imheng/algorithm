class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def traverse(self):
        if self.head is None:
            return []
        curr = self.head
        while curr:
            print(curr.item,end=" ")
            curr = curr.next
    def insertAtBegining(self,item):
        if self.head is None:
            self.head = item
            return
        item.next = self.head
        self.head = item
    def insertAtEnd(self,node):
        if self.head is None:
            self.head = node
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
    def inserMiddle(self,middle,node):
        if self.head is Node:
            self.head = node
            print("list is empty,insert at Begining")
            return
        curr = self.head
        while True:
            curr = curr.next
            if curr.item == middle:
                node.next = curr.next
                curr.next = node
                return



a = Node(1)
b = Node(2)
c = Node(3)
l = LinkedList()
l.head = a
a.next = b
b.next = c
l.traverse()
l.insertAtBegining(Node(0))
l.insertAtEnd(Node(5))
l.inserMiddle(3,Node("a"))
print("\n after inserting a item:\n")
l.traverse()
