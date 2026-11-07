# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Assuming above is already defined so no need to re-run.
# Re-cap:
# curr = curr.next moves curr to next box
# curr.next = x moves the arrow to point to x

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = ListNode()
        # Pointer which is blank defined.
        # Former solution had .dummyvariable object

        # Perhaps we can use the same logic as tailing it and 
        # At the same time doing some kind of count() calc.
        curr = head
        counter = 0
        while curr:
            print(curr.val)
            counter += 1
            curr = curr.next
            # This will establish how long the list is 

        print("1st While Loop Passed")

        prev = None
        curr = head 
        # newList = ListNode(prev)
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

        