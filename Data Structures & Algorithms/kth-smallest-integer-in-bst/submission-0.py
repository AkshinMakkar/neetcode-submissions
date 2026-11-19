class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def dfs(node):
            nonlocal count, result

            if not node:
                return None

            dfs(node.left)
            count += 1

            if k == count:
                result = node.val

            dfs(node.right)

        dfs(root)
        return result
