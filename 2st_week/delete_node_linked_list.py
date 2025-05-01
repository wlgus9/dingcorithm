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
    
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self.get_node(index-1)
            cur_node = self.get_node(index)
            
            prev_node.next = cur_node.next
        
linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(3)

print(linked_list.get_node(0).data)
print(linked_list.get_node(1).data)
print(linked_list.get_node(2).data)

linked_list.print_all()
linked_list.delete_node(0)
linked_list.print_all()
