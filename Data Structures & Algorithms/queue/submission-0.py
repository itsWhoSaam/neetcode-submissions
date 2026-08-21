class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left



    def isEmpty(self) -> bool:
        return self.left.next == self.right
        

    def append(self, value: int) -> None:
        node = ListNode(value)
        last_node = self.right.prev

        last_node.next = node
        node.prev = last_node

        node.next = self.right
        self.right.prev = node


        

    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        first_node = self.left.next

        self.left.next = node
        node.prev = self.left

        node.next = first_node
        first_node.prev = node
        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.right.prev
        value = last_node.val
        before_last = last_node.prev

        before_last.next = self.right
        self.right.prev = before_last



        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        target_node = self.left.next
        value = target_node.val

        next_node = target_node.next
        self.left.next = next_node
        next_node.prev = self.left
        return value
        
