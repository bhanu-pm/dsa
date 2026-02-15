# height balanced
# we go validating from the bottom up
# abs(maxdepth of left subtree - maxdepth of right subtree) <= 1
    # we have to check this condition at every node level



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        leftDepth, leftBool = self.depthBalanced(root.left)
        rightDepth, rightBool = self.depthBalanced(root.right)
        if leftBool and rightBool:
            if abs(leftDepth - rightDepth) <= 1:
                return True
        return False
        
    def depthBalanced(self, root):
        if not root:
            return 0, True
        if not root.left and not root.right:
            return 1, True
        leftDepth, leftBool = self.depthBalanced(root.left)
        rightDepth, rightBool = self.depthBalanced(root.right)
        if leftBool and rightBool:
            if abs(leftDepth - rightDepth) <= 1:
                return 1+max(leftDepth, rightDepth), True
        return 1+max(leftDepth, rightDepth), False