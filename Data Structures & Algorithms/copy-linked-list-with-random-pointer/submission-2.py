"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # edge case: if the LL is empty, return none -> remember head is the first node, so if we don't have a head then we can safely assume the list is empty 
        if not head:
            return None 
        
        # set curr = first node, head 
        curr = head 

        # old -> new 
        o_to_n = {}

        # make a copy of each node 
        while curr:
            n = Node(x=curr.val)
            o_to_n[curr] = n # add the new node to a hash map 
            curr = curr.next # move curr to the next node 
        
        curr = head # rebegin the head positioning
        
        while curr: # go through the linked list  
            new_node = o_to_n[curr] # set the new node 
            new_node.next = o_to_n[curr.next] if curr.next else None 
            new_node.random = o_to_n[curr.random] if curr.random else None 
            curr = curr.next 
        
        return o_to_n[head]
            
        