class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='')
            temp = temp.next
    def move_to_front(self):
        temp = self.head
        sec_last = None
        while temp and temp.next is not None:
            sec_last = temp
            temp = temp.next
        new_node = Node(sec_last.next.data)
        new_node.next = self.head
        self.head = new_node
        sec_last.next = None



if __name__ == '__main__':

    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)

    print('Linked list before swapping')
    llist.printlist()
    llist.move_to_front()
    print('Linked list after swapping')
    llist.printlist()