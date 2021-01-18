class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end = " ")
            temp=temp.next

def quicksort(head):
    a = []
    while head:
        a.append(head.data)
        head = head.next
    p = quick(a)
    for i in p:
        print(i, end=' ')

def quick(a):

    if len(a) <= 1:
        return a
    pivot = a.pop()
    left = []
    right = []
    for x in a:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quick(left) + [pivot] + quick(right)








if __name__ == '__main__':

    llist = LinkedList()
    llist.head = Node(1)
    second = Node(9)
    third = Node(3)
    fourth = Node(8)
    llist.head.next = second
    second.next = third
    third.next = fourth
    print('list before sorting')
    llist.printlist()
    print('\n')
    quicksort(llist.head)


