class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def maxDepth(root):
    if root is None:
        return 0
    else:
        lchildh = maxDepth(root.left)
        rchildh = maxDepth(root.right)
        return lchildh + 1 if lchildh > rchildh else rchildh + 1


# 函数调用格式如下
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

    res = maxDepth(a)
    print(res)


if __name__ == '__main__':
    main()
