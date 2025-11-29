# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')

        def dfs(root):
            if root is None:
                return float('-inf')

            left = dfs(root.left)
            right = dfs(root.right)

            if root.left is None and root.right is None:
                self.best = max(self.best, root.val)
                return root.val

            if root.right is None:
                leftbranch = max(root.val, root.val + left)
                self.best = max(self.best, leftbranch)
                return leftbranch
            if root.left is None:
                rightbranch = max(root.val, root.val + right)
                self.best = max(self.best, rightbranch)
                return rightbranch
            
            besthere = max(root.val, 
                           root.val + left, 
                           root.val + right, 
                           root.val + left + right, 
                           left, 
                           right)
            self.best = max(self.best, besthere)
            return max(root.val, root.val + left, root.val + right)
        dfs(root)
        return self.best