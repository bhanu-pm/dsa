# given BST***
# return kth smallest element
    # 1st smallest = smallest
    # 2nd smallest = [smallest, smaller, small]
        # smaller

# go to smallest possible value ?????
    # if root.right
        # with root.right as new root
            # find smallest possible including root
    # else:
        # go to root.left
            # if root.right
                # w root.right as new root
                    # find smallest possible val including root

# easier soln
    # go through left, root, right order and store them in an array
    # return k-1 th index val from array


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.elements = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return
        self.store(root)
        return self.elements[k-1]
        
    def store(self, root):
        if root is None:
            return
        
        if root.left:
            self.store(root.left)
        self.elements.append(root.val)
        
        if root.right is None:
            return
        else:
            self.store(root.right)