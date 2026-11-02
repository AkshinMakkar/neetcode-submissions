class Solution:
    def invertTree(self, root):
        # if we have nothing at root, return none to avoid an error
        if root is None:
            return None 
        
        # swap
        root.left, root.right = root.right, root.left 

        # recursively call the functions for left and right 
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return root, as the root is what is connected to the rest of the tree
        return root