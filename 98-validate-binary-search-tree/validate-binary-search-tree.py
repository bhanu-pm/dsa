# given root
    # return true if BST else false
# valid bst
    # if left subtree vals < node val
    # if right subtree vals > node val
    # left subtree is valid bst
    # right subtree is valid bst


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        rangee = [float('-inf'), float('inf')]
        if self.isbst(root.left, [float('-inf'), root.val]) and self.isbst(root.right, [root.val, float('inf')]):
            return True
        return False
    
    def isbst(self, root, r):
        if root is None:
            return True

        if root.val > r[0] and root.val < r[1]:
            if self.isbst(root.left, [r[0], root.val]) and self.isbst(root.right, [root.val, r[1]]):
                return True
        return False
