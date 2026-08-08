class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Case 1: both trees are empty
        if p is None and q is None:
            return True
        
        # Case 2: one tree is empty, the other is not
        if p is None or q is None:
            return False
        
        # Case 3: both nodes exist, but values are different
        if p.val != q.val:
            return False
        
        # Case 4: values are same, now compare left side and right side
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        
        return left_same and right_same