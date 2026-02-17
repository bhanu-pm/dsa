# binary tree given
# return nodes as seen if you are looking at tree from right side

# naive soln
    # if node.right
        # go right and return right
    # else:
        # go left and return right most

# a soln.
    # traverse BFS, queue
    # return the [-1] element of each level group


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque()
        q.append([root, 0])
        levels = []
        eachlevel = []
        current_level = 0
        while q:
            root, level = q.popleft()
            if level == current_level:
                eachlevel.append(root.val)
            elif level > current_level:
                current_level+=1
                levels.append(eachlevel)
                eachlevel = []
                eachlevel.append(root.val)
            if root.left:
                q.append([root.left, level+1])
            if root.right:
                q.append([root.right, level+1])
        levels.append(eachlevel)
        output = []
        for i in levels:
            output.append(i[-1])
        return output