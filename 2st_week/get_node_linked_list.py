class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        node_list = []
        cur = self.head
        
        while cur is not None:
            node_list.append(cur.data)
            cur = cur.next
            
        print(node_list)

    def get_node(self, index):
        cur = self.head
        cur_index = 0
        
        while cur_index != index:
            cur = cur.next
            cur_index += 1
        
        return cur

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(3)

print(linked_list.get_node(0).data)
print(linked_list.get_node(1).data)
print(linked_list.get_node(2).data)