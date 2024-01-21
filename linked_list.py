
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

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def get_item(self, item_from_position):
        if self.head is None:
            raise Exception("List is empty")

        for position, value in enumerate(self):
            if position == item_from_position:
                return position, value.data

        raise Exception("Node with position '%s' not found" % item_from_position)

    def get_items(self, start, end):
        if self.head is None:
            raise Exception("List is empty")

        if start < 0:
            raise Exception(f"Start number is less than 0:  {start}")

        count = 0
        items_of_list = []
        node = self.head
        while node is not None:
            if start <= count <= end:
                items_of_list.append(node.data)
            count += 1
            node = node.next
            if node is None and count < end:
                raise Exception(f"List are shorter than given End number {end}")
        return items_of_list

    def reverse_list(self):
        if self.head is None:
            raise Exception("List is empty")

        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self


llist = LinkedList(["a", "b", "c", "d","e"])
print(llist)
llist.add_first(Node('z'))
llist.add_last(Node('w'))
llist.add_after('e', Node('f'))
llist.add_before('w', Node('x'))
llist.remove_node('e')
iter_llist = iter(llist)

# Use the next function to retrieve each value
try:
    while True:
        value = next(iter_llist)
        print(value.data)
except StopIteration:
    pass


item = llist.get_item(1)
print(item)

items = llist.get_items(2, 5)
print(items)

reversed_linked_list = llist.reverse_list()
print(reversed_linked_list)