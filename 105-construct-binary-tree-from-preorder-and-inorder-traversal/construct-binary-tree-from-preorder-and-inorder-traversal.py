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
        for idx, num in enumerate(inorder):
            self.indict[num] = idx
        root = self.tree(preorder, inorder)
        return root

    def tree(self, preorder, inorder):
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        mid = self.indict[preorder[0]] - self.indict[inorder[0]]
        root.left = self.tree(preorder[1:mid+1], inorder[:mid])
        root.right = self.tree(preorder[mid+1:], inorder[mid+1:])
        return root