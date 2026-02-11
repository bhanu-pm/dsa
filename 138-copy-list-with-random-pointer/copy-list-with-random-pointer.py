# just a linked list, but it has an additional pointer
    # it could point to any node or null

# construct a deepcopy of the given ll
# have n nodes
    # with same values
# pointers pointing as expected
# essentially just a deepcopy
# return the head of copy

# 2 passes
# 1st pass, we create new nodes for the copy and store addresses of the corresponding copy in a hashmap
# 2nd pass, we assign the random pointers



"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        new = None
        top = None
        connections = dict()
        while node:
            if new is None:
                new = Node(node.val)
                top = new
            else:
                temp = Node(node.val)
                new.next = temp
                new = new.next
            connections[node] = new
            node = node.next
        
        node = head
        new = top
        while node:
            if node.random is None:
                new.random = None
            else:
                new.random = connections[node.random]
            new = new.next
            node = node.next
        return top