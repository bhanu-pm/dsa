# given BST
# find lowest node that is parent of both the given nodes
    # a node can be considered descendant of itself
    # p != q
    # p and q will def be present in BST

# its a BST, so unique values only
# maybe for each node, check if this subtree has both p and q nodes
# if yes (validity condition ????????)
    # store node, depth
# else
    # continue
# return node[max depth]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def __init__(self):
        self.max_depth = -1
        self.lca = 0
        self.depth = {}

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.depths(root)
        self.recurse(root, p, q)
        return self.lca
    
    def recurse(self, root, p, q):
        if root is None:
            return
        if self.insubtree(root, p) and self.insubtree(root, q):
            if self.depth[root.val] > self.max_depth:
                self.lca = root
        self.recurse(root.left, p, q)
        self.recurse(root.right, p, q)

    def insubtree(self, root, p):
        if root is None:
            return False
        if root.val == p.val:
            return True
        if self.insubtree(root.left, p) or self.insubtree(root.right, p):
            return True
        return False
    
    def depths(self, root):
        queue = deque()
        queue.append([root, 0])
        depth = 0
        while queue:
            node, level = queue.popleft()
            self.depth[node.val] = level

            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
