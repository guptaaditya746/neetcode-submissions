class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        result = None

        def inorder(node):
            nonlocal count, result

            if not node or result is not None:
                return

            # 1. Explore left subtree
            inorder(node.left)

            # 2. Stop if answer was found in left subtree
            if result is not None:
                return

            # 3. Process current node
            count += 1

            if count == k:
                result = node.val
                return

            # 4. Explore right subtree
            inorder(node.right)

        inorder(root)
        return result