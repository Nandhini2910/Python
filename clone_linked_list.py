class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbit = None
class LinkedList:
    def __init__(self):
        self.head = None
def clonelist(head):
    prev = head
    curr = head
    currnext = None
    temp = Node(curr.data)
    while  curr is not None:
        prev = curr
        currnext = curr.next
        temp.arbit = curr
        curr.next = temp
        curr = currnext
        temp.next =Node(currnext.data)
        temp = temp.next


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)


llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth


llist.head.arbit = third
second.arbit = llist.head
third.arbit = fifth
fourth.arbit = third
fifth.arbit = second






