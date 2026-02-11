# given two 'non-empty' ll, with 'non-negative' integers
# digits are stored in reverse order, so 125 becomes 5->2->1 (for ease of carry overs in addition)
# carry overs go to add to 'next' node
# return sum as a new linked list


# carry = 0
# node = None
# while ll1 and ll2
    # val = ll1.val + ll2.val + carry
    # carry = 0
    # if val>9:
        # remainder = val%10
        # carry = (val-remainder)/10
    # if node is None:
        # node = ListNode(remainder)
    # else:
        # temp = ListNode(remainder)
        # node.next = temp
        # node = node.next
    # ll1 = ll1.next
    # ll2 = ll2.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        node = head = None
        while l1 or l2 or (carry>0):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry
            digit = val%10
            carry = val//10
            if node is None:
                node = ListNode(digit)
                head = node
            else:
                temp = ListNode(digit)
                node.next = temp
                node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head