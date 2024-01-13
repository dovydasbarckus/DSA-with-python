
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return self.data
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             print(node)
#             nodes.append(node.data)
#             node = node.next
#         nodes.append("None")
#         return " -> ".join(nodes)
#
#
# llist = LinkedList()
# first_node = Node("a")
# llist.head = first_node
#
# second_node = Node("b")
# third_node = Node("c")
# first_node.next = second_node
# second_node.next = third_node


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


# Example usage:
elements_to_insert = [1, 2, 3, 4, 5]
linked_list = LinkedList(nodes=elements_to_insert)
print(linked_list)
