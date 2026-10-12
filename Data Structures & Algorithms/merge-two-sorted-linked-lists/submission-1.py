# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode() # a new "dummy node to store our output"
        cur = d # we are starting our current node to the begining, which is the dummy node 
        
        # below, we are just confirming that there are nodes in each list 
        while list1 and list2: 
            if list1.val < list2.val: 
                cur.next = list1 # move the list 1 value from a hook to the previous node 
                cur = list1 # move our current value to the new one 
                list1 = list1.next # now move over to the next node in list 1 since we added it to the dummy node via a hook
            else: # same thing as list 1, but for list2 
                cur.next = list2 
                cur = list2 
                list2 = list2.next 
            
            # edge case if we just have elements in one of these lists 
        if list1: 
            cur.next = list1
        else:
            cur.next = list2
            
        return d.next # return all values after d 
            
