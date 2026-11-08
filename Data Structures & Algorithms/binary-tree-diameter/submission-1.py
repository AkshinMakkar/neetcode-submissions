
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(root):
            nonlocal diameter 
            if root is None:
                return 0 
            
            left = height(root.left)
            right = height(root.right)

            diameter = max(diameter, left + right)
            return max(left, right) + 1 
        
        height(root)
        return diameter
            


        
        
