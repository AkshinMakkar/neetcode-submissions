
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def has_subtree(root):
            if not root:
                return False

            if sameTree(root, subRoot):
                return True

            return has_subtree(root.left) or has_subtree(root.right)

        if subRoot is None:
            return True

        return has_subtree(root)
