# given Binary** Tree
# if in path from root to X, all node.vals < X
    # X is good node
# return no. of good nodes

# we need to go through all nodes
    # verify if its a good node
        # seperate method for verification

# verification
    # monotonically decreasing stack???
        # cause any value >= root pops all other values
        # i assume it only works for linear Data stuctures, cause branching in trees, it might be complicated
    # instead of calc. verification, what if we track verification while traversal itself
        # good_count
        # max_encountered_node
            # if current_node >= max_encountered_node:
                # good_count += 1
        # if reached leaf, backtrack and go right
            # how to update max_encountered_node????????????
                # can't keep track of seen, cause not unique vals


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.good_count = 0
        self.max_seen = 0
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.max_seen = root.val
        self.good_count = 1
        if root.left:
            self.recurse(root.left)
        self.max_seen = root.val
        if root.right:
            self.recurse(root.right)
        return self.good_count
    
    def recurse(self, root):
        if root is None:
            return
        if root.val >= self.max_seen:
            self.good_count += 1
            self.max_seen = root.val
        temp = self.max_seen
        if root.left:
            self.recurse(root.left)
        self.max_seen = temp
        if root.right:
            self.recurse(root.right)