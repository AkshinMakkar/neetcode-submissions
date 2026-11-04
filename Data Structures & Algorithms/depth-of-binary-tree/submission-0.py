# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0 
        
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            
        return 1 + max(left, right)
        
        # time complexity = O(n) in the worst case as we have to check every nodes 
        # Space O(h) where h is the height 
        # in the worst case we are storing h total 

        