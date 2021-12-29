class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root):
        def _rob(node):
            res = [0, 0]
            if not node:
                return res
            left = _rob(node.left)
            right = _rob(node.right)
            res[0] = max(left[0], left[1]) + max(right[0], right[1])
            res[1] = node.val + left[0] + right[0]
            return res
        res = _rob(root)
        return max(res[0], res[1])
