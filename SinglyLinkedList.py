class Node:
    def __init__(self, data):
        """Initialize a node with data and no next node."""
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node with the given data at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        """Delete the first node with the given data."""
        current = self.head

        # If the head node itself holds the key to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        # If the key was not present in the list
        if not current:
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

    def traverse(self):
        """Traverse and print the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Testing the SinglyLinkedList class
if __name__ == "__main__":
    sll = SinglyLinkedList()
    
    # Insert nodes
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_beginning(0)
    
    # Print the linked list
    print("Linked List after insertion:")
    sll.traverse()
    
    # Delete a node
    sll.delete_node(2)
    
    # Print the linked list after deletion
    print("Linked List after deleting node with value 2:")
    sll.traverse()
    
    # Delete head node
    sll.delete_node(0)
    
    # Print the linked list after deleting head node
    print("Linked List after deleting head node with value 0:")
    sll.traverse()
    
    # Delete a non-existent node
    sll.delete_node(99)
    
    # Print the linked list after attempting to delete a non-existent node
    print("Linked List after attempting to delete non-existent node with value 99:")
    sll.traverse()
