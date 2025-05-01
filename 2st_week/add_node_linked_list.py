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
    
    def add_node(self, index, value):
        new_node = Node(value) # 새로운 노드 생성
        
        if index == 0: # 인덱스가 0이면 head 교체
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.get_node(index-1) # 추가할 인덱스의 앞의 노드(index-1) 가져오기 (앞에 노드에서 뒤에 새로 추가해 줘야 하니까)
            
            next_node = prev_node.next # 연결되어 있던 값(next)은 미리 저장 (안 하면 그 다음에 어떤 노드가 연결되어 있었는지 모름)
            
            prev_node.next = new_node # next에 새로운 노드 추가
            new_node.next = next_node # 추가된 노드의 next에는 기존에 연결되어 있었던 노드 연결

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(3)

print(linked_list.get_node(0).data)
print(linked_list.get_node(1).data)
print(linked_list.get_node(2).data)

linked_list.print_all()
linked_list.add_node(1, 6)
linked_list.print_all()
linked_list.add_node(0, 9)
linked_list.print_all()
