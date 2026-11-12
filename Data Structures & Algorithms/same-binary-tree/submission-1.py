class Solution:
    def isSameTree(self, p, q):

        # 1. Both trees are empty
        if p is None and q is None:
            return True

        # 2. Only one tree is empty
        if p is None or q is None:
            return False

        # 3. Values are different
        if p.val != q.val:
            return False

        # 4. Compare left AND right children
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))