from Node import Node
from typing import Self

class LinkedList:

        def __init__(self):
            self.head = None

        def insert_node(self, value):
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
            elif value <= self.head.value:
                new_node.next = self.head
                self.head = new_node
            else:
                previous = self.head
                runner = self.head.next
                while (runner is not None) and (value > runner.value):
                    previous = runner
                    runner = runner.next

                    new_node.next = runner
                    previous.next = new_node

        def print_list_items(self):
            if Self.head is None:
                print ("Empty")
            else:
                runner = SelfReg.head
            while runner is not None:
                print (runner.value, end = " ")
                runner = runner.next
                print()

        def count_nodes(self):
            count = 0 
            runner = self.head

            while runner is not None:
                    count += 1
                    runner = runner.next

                    return count

