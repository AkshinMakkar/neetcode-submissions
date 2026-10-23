# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # make a new list node to store the result in 
        d = ListNode()
        # set make current variable to move throughout the dummy 
        curr = d 
        carry = 0 # the carry is what we will use to move a number because we can only put on digit inside of a node 

        # say we have [1, 2, 3] = l1, and [4, 5, 6] = l2, we keep going because as long as we have some numbers left, we can add that to the dummy node 
        while l1 or l2 or carry:
            # we want to extract the values from the list if it exists, if not, then give 0 
            if l1: 
                value1 = l1.val 
            else:
                value1 = 0
            if l2:
                value2 = l2.val 
            else:
                value2 = 0 

            # this will give us the total amount we want
            total = value1 + value2 + carry
            carry = total // 10 # the carry will figure out what we move on
            digit = total % 10 # digit is what we will add at the current node 

            # add digit to listnode 
            curr.next = ListNode(digit)
            curr = curr.next 
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next 
            
        return d.next 
            
            


        

        

            

        