# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    res = []
    if not root:
        return res

    nodelist = [root]
    level, levelnode = [], []
    while nodelist:
        node = nodelist.pop(0)
        if node:
            level.append(node.val)
            if node.left:
                levelnode.append(node.left)
            if node.right:
                levelnode.append(node.right)
        if not nodelist:
            res.append(level)
            level = []
            nodelist = levelnode
            levelnode = []
    return res


def main():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    res = levelOrder(a)
    print(res)


if __name__ == '__main__':
    main()
