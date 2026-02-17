# group all nodes of a level together
# return list of groups
# using queue or BFS gives level wise nodes


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append([root, 0])
        output = []
        current_level = 0
        group = []
        
        while queue:
            root, level = queue.popleft()
            if level == current_level:
                group.append(root.val)
            if level > current_level:
                current_level += 1
                output.append(group)
                group = []
                group.append(root.val)

            if root.left:
                queue.append([root.left, level+1])
            if root.right:
                queue.append([root.right, level+1])

        output.append(group)
        return output