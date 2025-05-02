# 링크드 리스트의 끝에서 K번째 값을 반환하시오.
# [6] -> [7] -> [8] -> [9] -> [10]
# 이런 링크드 리스트가 입력되었을 때, 
# 끝에서 2번째 값은 9를 반환해야 합니다!

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

    def get_kth_node_from_last(self, k):
        # 방법 1. 각 노드들을 배열에 담아 인덱스로 가져오기
        # cur = self.head
        # arr = []
        
        # while cur is not None:
        #     arr.append(cur)
        #     cur = cur.next
        
        # return arr[-k]
        
        # 방법 2. k만큼의 간격을 두는 노드 생성
        slow = self.head
        fast = self.head
        
        for i in range(k): # fast 노드는 k만큼의 간격을 둘 수 있게 미리 이동
            fast = fast.next
            
        while fast is not None: # fast 노드가 None이 아닐 때까지(끝에 도달할 때까지) 반복
            slow = slow.next
            fast = fast.next
            
        # 끝에 도달했으면 slow는 끝에서 k만큼 떨어진 노드가 되는 것
        return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)

print(linked_list.get_kth_node_from_last(2).data)