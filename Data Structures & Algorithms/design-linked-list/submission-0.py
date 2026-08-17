class ListNode:

    def __init__(self, val =0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.length = 0
        

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        if index < 0 or index >= self.length:
            return -1
        while i < index:
            if curr:
                curr = curr.next
                i += 1
        return curr.val


        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1


        

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        new_node = ListNode(val)
        curr.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        if index > self.length:
            return 
        i = 0
        while i < index:
            if curr.next:
                curr = curr.next
                i+= 1
        new_node = ListNode(val)
        new_node.next = curr.next 
        curr.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        curr = self.head
        i = 0
        while i < index:
            if curr.next:
                curr = curr.next
                i += 1
        curr.next = curr.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)