class Node:
    def __init__(self, data):
        """Initialize a node with data and no next or previous node."""
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        """Insert a new node with the given data at the beginning of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, key):
        """Delete the first node with the given data."""
        current = self.head

        while current:
            if current.data == key:
                if current == self.head:  # Node to delete is head
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                if current == self.tail:  # Node to delete is tail
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                if current.prev:  # Node is in the middle
                    current.prev.next = current.next
                if current.next:  # Node is in the middle
                    current.next.prev = current.prev
                return
            current = current.next

    def traverse_forward(self):
        """Traverse and print the list from head to tail."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """Traverse and print the list from tail to head."""
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Testing the DoublyLinkedList class
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    # Insert nodes
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_beginning(0)
    
    # Print the linked list
    print("Doubly Linked List after insertion:")
    dll.traverse_forward()
    
    # Print the linked list in reverse
    print("Doubly Linked List in reverse:")
    dll.traverse_backward()
    
    # Delete a node
    dll.delete_node(2)
    
    # Print the linked list after deletion
    print("Doubly Linked List after deleting node with value 2:")
    dll.traverse_forward()
    
    # Delete head node
    dll.delete_node(0)
    
    # Print the linked list after deleting head node
    print("Doubly Linked List after deleting head node with value 0:")
    dll.traverse_forward()
    
    # Delete tail node
    dll.delete_node(3)
    
    # Print the linked list after deleting tail node
    print("Doubly Linked List after deleting tail node with value 3:")
    dll.traverse_forward()
    
    # Delete a non-existent node
    dll.delete_node(99)
    
    # Print the linked list after attempting to delete a non-existent node
    print("Doubly Linked List after attempting to delete non-existent node with value 99:")
    dll.traverse_forward()
