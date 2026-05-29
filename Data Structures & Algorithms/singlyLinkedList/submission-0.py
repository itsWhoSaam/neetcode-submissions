class ListNode:
    
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # Dummy Node 
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next # .next because self.head is already pointing to dummy pointer with default value -1, .next iterates pointer to next listnode element
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # Index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if new_node.next == None:
            self.tail = new_node


    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
            

    def remove(self, index: int) -> bool:
        if index < 0:
            return False

        prev_node = self.head
        curr_node = self.head.next
        i = 0

        while curr_node is not None and i != index:
            prev_node = curr_node
            curr_node = curr_node.next
            i += 1

        if curr_node is None:  # index out of bounds
            return False

        if curr_node.next is None:  # If we are removing the last node
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next = curr_node.next

        # Special case for removing the head (not the dummy head, but the first actual element)
        if prev_node == self.head and self.head.next is None:
            self.tail = self.head

        return True

            

    def getValues(self) -> List[int]:
        lst = []
        curr_node = self.head.next
        while curr_node != None:
            lst.append(curr_node.val)
            curr_node = curr_node.next
        return lst
