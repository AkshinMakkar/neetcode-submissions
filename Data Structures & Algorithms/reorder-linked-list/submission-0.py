# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# REVIEW 

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

# make a slow and fast pointer to help us split the list in half 
# slow increments by 1 
# high increments by 2 
        slow = head 
        fast = head 
    
# make only move the pointers if fast is on a node and a node exists beside it 
# this ensures we don't have an infinite loop 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

# once we exist the while loop, start our second list at the next node from slow
# slow.next makes sure we stop at slow, and not the node next to it 
        second = slow.next 
        slow.next = None 

# now, reverse the list

        prev = None # initalize prev 
        curr = second # curr = second, the head (first node)

        while curr:  # keep iterating through 
            tmp = curr.next # use temp to save the node beside it 
            curr.next = prev # point curr to prev, the other side 
            prev = curr # move a node to make prev - curr 
            curr = tmp # start the next curr iteration at temp, where we stored it 
             


        second = prev # we need to start second at the prev node to ensure they are on the same node 
        first = head 

# merge: 
        while second: 
            tmp1 = first.next 
            tmp2 = second.next 
            first.next = second 
            second.next = tmp1
            first = tmp1
            second = tmp2
        
        


        