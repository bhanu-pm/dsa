# given two roots
# if subroot is subtree of root
    # return true
# else return false
# a tree could be a subtree of itself too

# for each root node, check if its same as subroot


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if root.val == subRoot.val:
            if self.sametree(root.left, subRoot.left) and self.sametree(root.right, subRoot.right):
                return True
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        return False
    
    def sametree(self, root, subroot):
        if not subroot and not root:
            return True
        if not root or not subroot:
            return False
        
        if root.val == subroot.val:
            if self.sametree(root.left, subroot.left) and self.sametree(root.right, subroot.right):
                return True
        return False