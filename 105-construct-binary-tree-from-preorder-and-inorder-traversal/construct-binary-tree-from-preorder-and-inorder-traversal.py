# preorder and inorder given, construct a binary tree from them

# preorder tells us, root comes first
# from inorder, left of root is left subtree, right of root is right subtree

# pop first element from preorder,
    # left of first element in inorder, in left subtree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preorder = []
        self.inorder = []
        self.indict = dict()

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        self.preorder = preorder
        self.inorder = inorder
        n = len(preorder)
        for idx, num in enumerate(inorder):
            self.indict[num] = idx
        root = self.tree(0, n, 0, n)
        return root

    def tree(self, pleft, pright, ileft, iright):
        if not self.preorder[pleft:pright] or not self.inorder[ileft:iright]:
            return
        root = TreeNode(self.preorder[pleft])
        relative = self.indict[self.inorder[ileft]]
        mid = self.indict[self.preorder[pleft]] - relative
        root.left = self.tree(pleft+1, pleft+mid+1, ileft, ileft+mid)
        root.right = self.tree(pleft+mid+1, pright, ileft+mid+1, iright)
        return root