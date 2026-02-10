# we need to have two pointers converging from either ends
# since, its a single linked list
    # we have to reverse the linked list and make a copy????
        # we can just reverse the 2nd half of the ll
        # how to find 2nd half????
            # we can use fast and slow pointers to find mid

# using fast and slow pointers to find mid point
# reverse linked list from after mid point
# use two pointers to move them around and arrange alternatively


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        if not head.next:
            return
        if not head.next.next:
            return
        # use fast and slow pointers to find midpoint
        top = head
        slow = head
        fast = head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
            else:
                break
        # reverse the sll part that comes after slow
        head = slow.next
        slow.next = None
        new = None
        while head:
            if not new:
                new = head
                head = head.next
                new.next = None
            else:
                temp = head.next
                head.next = new
                new = head
                head = temp
        # rearrange to form final order
        i = top
        j = new
        head = None
        while i:
            if not head:
                head = i
            else:
                head.next = i
                head = head.next
            i = i.next
            head.next = j
            if j:
                j = j.next
            head = head.next
        head = top