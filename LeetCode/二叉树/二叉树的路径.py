class Solution:
    def binaryTreePaths(self, root):
        def DFS(root):
            if not root:
                return 
            path.append(str(root.val)) 
            if not root.right and not root.left:
                res.append("->".join(path))
            DFS(root.left)
            DFS(root.right)
            path.pop()

        path = list()
        res = list()
        DFS(root)
        return res
