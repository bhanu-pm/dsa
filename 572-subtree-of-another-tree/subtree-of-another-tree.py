# root and subroot given

# naive solution
# if node.val == subroot.val
    # if node.left.val == subroot.left.val
        # if node.right.val == subroot.right.val
            # if node.left.left is None and node.left.right is None and node.right.left is None and node.right.right is None:
                # true
# else
    # continue

# if node.val == subroot.val
    # 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        stack = deque()
        stack.append(root)
        while stack:
            root = stack.pop()
            if root is None:
                continue
            if root.val == subRoot.val:
                if self.sameTree(root, subRoot):
                    return True
            stack.append(root.right)
            stack.append(root.left)
        return False

    def sameTree(self, p, q):
        stackp = deque()
        stackq = deque()
        stackp.append(p)
        stackq.append(q)
        while stackp and stackq:
            p = stackp.pop()
            q = stackq.pop()
            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            stackp.append(p.right)
            stackq.append(q.right)
            stackp.append(p.left)
            stackq.append(q.left)
        return True