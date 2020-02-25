import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList



        

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = DoublyLinkedList(value)
            self.size += 1
        else:
            new_node = DoublyLinkedList(value)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
            self.size += 1
        
        

    def pop(self):
        if self.head is None:
            return None
        else:
            value_removed = self.head
            self.head = self.head.next
            if self.size == 1:
                self.head = None
            else:
                self.head.prev is None
            self.size -= 1

            return value_removed
        

    def len(self):
        return self.size
        
