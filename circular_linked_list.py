
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))

    def traverse_with_list(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        nodes = []
        node = starting_point
        while node is not None and (node.next != starting_point):
            nodes.append(node)
            node = node.next
        nodes.append(node)
        return nodes

    def get_values(self, starting_point=None):
        nodes_data = self.traverse_with_list(starting_point)
        print(" -> ".join(map(str, nodes_data)))

    def traverse_values(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        nodes_data = []
        node = starting_point
        while node is not None and (node.next != starting_point):
            nodes_data.append(node.data)
            node = node.next
        nodes_data.append(node.data)
        return nodes_data

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


circular_llist = CircularLinkedList()
circular_llist.print_list()

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
d.next = a


circular_llist.head = a
circular_llist.print_list(a)
circular_llist.print_list(a)
circular_llist.print_list(b)
circular_llist.print_list(d)


result = circular_llist.traverse_with_list(c)
print(result)

circular_llist.get_values(c)

node_values = circular_llist.traverse_values(c)
print(node_values)


iter_llist = iter(circular_llist)
# Use the next function to retrieve each value
for _ in range(6):
    value = next(iter_llist)
    print(value.data)
