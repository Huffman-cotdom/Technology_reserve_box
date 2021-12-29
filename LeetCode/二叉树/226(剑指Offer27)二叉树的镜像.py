# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root


root = [4, 2, 7, 1, 3, 6, 9]
root = TreeNode(root)
# print(root.val)
print(Solution().invertTree(root).val)
