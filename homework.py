# Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def print_list(self):
        if self.start_node is None:
            print("Список пустой")
            return
        else:
            n = self.start_node
        while n is not None:
            print(n.data, " ")
            n = n.ref

    def append(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def reverse(self):
        prev_item = None
        n = self.start_node
        while n is not None:
            next_item = n.ref
            n.ref = prev_item
            prev_item = n
            n = next_item
            self.start_node = prev_item


lst = LinkedList()
lst.append(1)
lst.append(3)
lst.append(5)
lst.append(7)
lst.append(9)
lst.print_list()
lst.reverse()
lst.print_list()
