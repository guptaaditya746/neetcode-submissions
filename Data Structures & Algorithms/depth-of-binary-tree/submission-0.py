class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case: empty tree has depth ___
        if root is None:
            return 1

        # ask left subtree for its depth
        left_depth = self.maxDepth(root.left)

        # ask right subtree for its depth
        right_depth = self.maxDepth(root.right)

        # current node adds 1 level above the deeper side
        return 1 + max(left_depth, right_depth)