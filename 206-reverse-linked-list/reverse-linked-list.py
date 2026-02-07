# reverse
# output a ll reversed
# stored = None
# while head
    # if stored:
        # temp = head.next
        # head.next = stored
    # else
        # temp = head.next
        # stored = head
        # stored.next = None
        # head = head.next
# return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stored = None
        while head:
            temp = head.next
            if stored:
                head.next = stored
                stored = head
            else:
                stored = head
                stored.next = None
            head = temp
        return stored