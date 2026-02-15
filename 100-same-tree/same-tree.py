# they are same if same structure and node values
# recursive solution might be a bit unintuitive
    # iterative
# compare all 3 conditions left.val, right.val, root.val
    # pointers shouldn't be same, so we compare values
# store root in stack
    # store root.right in stack
        # process root.left
        # root = root.left
            # if root.left or root.right
                # store root.right in stack
                    # process root.left

# from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p:
        #     if not q:
        #         return True
        #     return False
        # if not q:
        #     if p:
        #         return False
        # stackp = deque()
        # stackq = deque()
        # stackp.append(p)
        # stackq.append(q)
        # while stackp and stackq:
        #     p = stackp.pop()
        #     q = stackq.pop()
        #     if p is None and q is None:
        #         continue
        #     if p is None or q is None:
        #         return False
        #     if p.val != q.val:
        #         return False
        #     if not p.left and not p.right:
        #         if not q.left and not q.right:
        #             pass
        #         else:
        #             return False
        #     if not q.left and not q.right:
        #         if not p.left and not p.right:
        #             pass
        #         else:
        #             return False

        #     stackp.append(p.right)
        #     stackq.append(q.right)
        #     stackp.append(p.left)
        #     stackq.append(q.left)
        # return True

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
        return False