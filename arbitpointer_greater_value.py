#https://ide.geeksforgeeks.org/Xd8WFQqIkn
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbit = None


def reverselist(head):
    prev = None
    curr = head
    cnext = None
    while curr != None:
        cnext = curr.next
        curr.next = prev
        prev = curr
        curr = cnext
    head = prev
    return head


def arbitpointer(head):
    head = reverselist(head)
    maxval = head
    temp = head.next
    while temp != None:
        temp.arbit = maxval
        if maxval.data < temp.data:
            maxval = temp
        temp = temp.next
    head = reverselist(head)
    return head


def printlist(head):
    while (head.next != None):
        print(head.data, head.arbit.data)
        head = head.next
    print(head.data, 'None')


head = Node(5)
second = Node(10)
third = Node(2)
fourth = Node(3)

head.next = second
second.next = third
third.next = fourth

temp = arbitpointer(head)
printlist(temp)






