class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.dummy = Node()
        self.next = None
        self.size = 0
        # If c = LinkedList(). self --> c.
        # i.e. self is a placeholder only of course.
        # Head = First Node
        # Tail = Last Node
        # Node combines .data and .next
    
    def get(self, index: int) -> int:
        # Note: 0-indexed, so:
        # Edge nr1
        if index < 0 or index >= self.size:
            return -1

        curr = self.dummy.next 
        for _ in range(index):
            curr = curr.next # Keeps going until index (input arg) is reached
        return curr.data
        
    def insertHead(self, val: int) -> None:
        # Recall: Head is First Node.
        new = Node(val)
        new.next = self.dummy.next
        self.dummy.next = new
        self.size +=1
        return

    def insertTail(self, val: int) -> None:
        new = Node(val)

        curr = self.dummy
        placeholder = curr
        while curr.next is not None:
            curr = curr.next
            # Tail is reached at the end of the loop

        curr.next = Node(val)
        # If we want a link back then we can use:
        # new.next = placeholder

        self.size +=1
        return
        
    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        curr = self.dummy
        for _ in range(index):
            curr = curr.next # Keeps going until index (input arg) is reached
         
        curr.next = curr.next.next # As simple as skipping one over?

        self.size -= 1
        return True
        
    def getValues(self) -> List[int]:
        curr = self.dummy.next
        values = []
        for i in range(self.size):
            values.append(curr.data)
            curr = curr.next            

        return values

"""
Additional Notes:
- Think about edge cases and practice doubly LL with talking.
"""
