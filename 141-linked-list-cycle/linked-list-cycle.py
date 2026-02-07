# use a set to store values
# if value in set, we got a cycle?

# using two pointers
# left = head
# right = head.next
# while True:
    # if left == right.next:
        # return True
    # if 
    # right = right.next
    # 



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        right = head.next
        if right:
            right = right.next
        while right:
            if right.next == head or right == head:
                return True
            head = head.next
            right = right.next
            if right:
                right = right.next
            else:
                break
        return False