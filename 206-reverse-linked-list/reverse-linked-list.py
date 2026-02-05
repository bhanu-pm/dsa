# time complexity = O(N) obviously
# in a loop go through each element

# prev is previous node
# node points to current node
# temp = node.next
# node.next = prev
# if temp:
    # prev = node
    # node = temp
# else:
    # break


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev = None

        while True:
            temp = head.next
            head.next = prev
            if temp:
                prev = head
                head = temp
            else:
                break
        
        return head