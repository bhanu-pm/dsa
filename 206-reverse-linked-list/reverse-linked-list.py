# head given
# new = None
# while head:
    # if not new:
        # new = head
        # head = head.next
        # new.next = None
    # else:
        # temp = head.next
        # head.next = new
        # new = head
        # head = temp

###############
# new = head
# head = head.next
# new.next = None
# while head:
    # temp = head.next
    # head.next = new
    # new = head
    # head = temp


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        new = head
        head = head.next
        new.next = None
        while head:
            temp = head.next
            head.next = new
            new = head
            head = temp
        return new