class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # To print all the elements of the Linked List

                
    def PrintList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(3)
    llist.push(2)
    llist.push(6)
    llist.push(5)
    llist.push(11)
    llist.push(10)
    llist.push(15)
    llist.push(12)

    print("Given Linked List: ", end=' ')
    llist.PrintList()
    print("\n\nDeleting node 10:")
    llist.deleteNode(10)
    print("Modified Linked List: ", end=' ')
    llist.PrintList()
    print("\n\nDeleting first node")
    llist.deleteNode(12)
    print("Modified Linked List: ", end=' ')
    llist.PrintList()