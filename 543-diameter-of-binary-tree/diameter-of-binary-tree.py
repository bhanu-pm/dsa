# diam is length of longest path btw any 2 nodes

# depth of that subtree should be returned above
# longest path, depth of left subtree + depth of right subtree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.longest = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 0

        self.depth(root)

        return self.longest
    
    def depth(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1

        left = self.depth(root.left)
        right = self.depth(root.right)
        self.longest = max(self.longest, left+right)
        
        return 1+max(left, right)