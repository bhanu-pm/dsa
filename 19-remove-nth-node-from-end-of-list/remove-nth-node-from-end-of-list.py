# remove nth from END of single linked list
# return its head

# go through list and find length
# idx = length - given 'n'
# remove the idx
    # idx - 1.next = idx.next

# i = 0
# while i < idx:
    # temp = head
    # head = head.next
    # i+=1
# else:
    # head = head.next
    # temp.next = head
    # head = top
# return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        top = head
        while head:
            head = head.next
            length+=1
        
        idx = length-n
        i = 0
        head = top
        temp = None
        while i<idx:
            temp = head
            head = head.next
            i+=1
        else:
            if temp:
                head = head.next
                temp.next = head
                head = top
            else:
                head = head.next
        return head