class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def push(head , data):
    new_node = Node(0)
    new_node.data = data
    new_node.next = head
    head = new_node
    return head


def tripletsum(head1, head2, head3, givenNumber):
    a = headA

    # Traverse through all nodes of a
    while a is not None:

        b = headB
        c = headC

        # For every node of list a, prick two nodes
        # from lists b abd c
        while b is not None and c is not None:

            # If this a triplet with given sum, print
            # it and return true
            sum = a.data + b.data + c.data
            if sum == givenNumber:

                print ("Triplet Found: ", a.data, " ", b.data, " ", c.data)
                return True

            # If sum of this triplet is smaller, look for
            # greater values in b
            elif sum < givenNumber:
                b = b.next
            else:  # If sum is greater, look for smaller values in c
                c = c.next

        a = a.next  # Move ahead in list a

    print("No such triplet")
    return False


headA = None
headB = None
headC = None

# create a linked list 'a' 10.15.5.20
headA = push(headA, 20)
headA = push(headA, 4)
headA = push(headA, 15)
headA = push(headA, 10)

# create a sorted linked list 'b' 2.4.9.10
headB = push(headB, 10)
headB = push(headB, 9)
headB = push(headB, 4)
headB = push(headB, 2)

# create another sorted
# linked list 'c' 8.4.2.1
headC = push(headC, 1)
headC = push(headC, 2)
headC = push(headC, 4)
headC = push(headC, 8)

givenNumber = 25

tripletsum(headA, headB, headC, givenNumber)
