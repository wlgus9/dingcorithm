class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
node = Node(5)
print(node.data, node.next)

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        
    # LinkedList의 가장 끝에 있는 노드에 새로운 노드 연결
    def append(self, value):
        cur = self.head
        
        while cur.next is not None:
            cur = cur.next
            
        cur.next = Node(value)
        
    # 현재 있는 노드 출력
    def print_all(self):
        node_list = []
        cur = self.head
        
        while cur is not None:
            node_list.append(cur.data)
            cur = cur.next
            
        print(node_list)
        
linked_list = LinkedList(5)
print(linked_list.head.data)

linked_list.append(12)
linked_list.append(8)

linked_list.print_all()