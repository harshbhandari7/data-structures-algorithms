class Node:
	def __init__(self, val):
		self.value = val
		self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        
        current_node = self.head
        idx = 0
        while idx < index:
            current_node = current_node.next
            idx += 1
        
        return current_node.value    
    
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        current_node = self.head
        new_node = Node(val)

        # if index is 0 or less than, we add the in the front
        if index <= 0:
            self.head = new_node
            new_node.next = current_node
        else:
            idx = 0
            while idx < (index-1):
                current_node = current_node.next
                idx += 1

            new_node.next = current_node.next
            current_node.next = new_node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        # handling index out of bound
        if index < 0 or index >= self.length:
            return

        current_node = self.head

        if index == 0:
            self.head = current_node.next
        else:
            idx = 0
            while idx < (index-1):
                current_node = current_node.next
                idx += 1
                
            current_node.next = current_node.next.next

        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)