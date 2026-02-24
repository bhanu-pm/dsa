# inplace reversal

# traverse the head, through the ll
# while head.next
    # store head.next
    # reverse head to point to previous
    # current node is now the new previous
    # new head is stored head.next
# return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev