class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = Node(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end="")

        node = node.next

        if node:
            print(sep, end="")
    print()  

def deleteDuplicates(head):
    curr = head

    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head

my_list = SinglyLinkedList()

my_list.insert_node(1)
my_list.insert_node(1)
# my_list.insert_node(20)
# my_list.insert_node(30)

print_singly_linked_list(my_list.head, " -> ")
new_list = deleteDuplicates(my_list.head)
print_singly_linked_list(new_list, " -> ")