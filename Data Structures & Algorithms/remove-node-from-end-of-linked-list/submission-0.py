# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy node
        d = ListNode()
        # point the dummy node to head 
        d.next = head 
        # make two pointers, starting at the dummy node
        a = d 
        b = d 

        # because we added the dummy node at the start, to get behind the node we want to delete 
        # go in range(n+1)
        for l in range(n+1):
            a = a.next
        
        # now set behind to go right before the node we want to delete
        while a: 
            b = b.next
            a = a.next
            
            # once we are behind the node we want to delete, make that node point to the node after the next
        b.next = b.next.next
        
        
        return d.next
