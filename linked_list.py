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
            print(curr.item)
            curr = curr.next

a = Node(1)
b = Node(2)
c = Node(3)
l = LinkedList()
l.head = a
a.next = b
b.next = c
l.traverse()
