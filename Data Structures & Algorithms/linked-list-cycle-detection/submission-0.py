# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we want to use the slow fast algorithm for this problem
        # make a dummy node to point to help out
        d = ListNode()
        d.next = head # point the dummy node to the head of the linked list
     # start the slow and fast pointers to the location of the dummy node initially

        slow = d
        fast = d

        # we want to see if it can safely move two nodes from where it currently is
        while fast and fast.next:
            fast = fast.next.next # increase by 2
            slow = slow.next # increase by 1

            if slow is fast: # if they meet at the same node, return True
                return True

        return False # if the while loop terminates without true, return False 
            
