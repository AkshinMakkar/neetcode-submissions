
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # 1. If the tree is empty, return an empty list
        if not root:
            return []

        # 2. Store our final answer here
        result = []

        # 3. Create a queue starting with the root node
        queue = deque([root])

        # 4. Keep going while there are nodes in the queue
        while queue:

            # 5. Count how many nodes are in the current level
            level_size = len(queue)

            # 6. Store the values for this level
            level = []

            # 7. Process only the nodes in the current level
            for i in range(level_size):

                # 8. Remove the first node from the queue
                node = queue.popleft()

                # 9. Add its value to the current level
                level.append(node.val)

                # 10. Add the left child if it exists
                if node.left:
                    queue.append(node.left)

                # 11. Add the right child if it exists
                if node.right:
                    queue.append(node.right)

            # 12. Add the completed level to our result
            result.append(level)

        # 13. Return all levels
        return result

            
            

            
        
            
        

           
            