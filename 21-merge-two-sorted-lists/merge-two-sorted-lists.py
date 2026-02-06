# two sorted linked lists given,
# make a new ll, merging together both given lists, in given sorting order
# ascending order

# mylist = ListNode() # this will be the head
# myptr # will go through my linked list
# while list1 and list2:
    # if list1.val <= list2.val:
        # node = ListNode(list1.val)
        # list1 = list1.next
    # else:
        # node = ListNode(list2.val)
        # list2 = list2.next
    # myptr.next = node
    # myptr = myptr.next
# else:
    # if list1:
        # myptr.next = list1
    # elif list2:
        # myptr.next = list2
# return mylist


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mylist = None
        myptr = None
        while list1 and list2:
            if list1.val <= list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            
            if mylist:
                myptr.next = node
                myptr = myptr.next
            else:
                mylist = node
                myptr = mylist
        else:
            if list1:
                if mylist:
                    myptr.next = list1
                else:
                    mylist = list1
            elif list2:
                if mylist:
                    myptr.next = list2
                else:
                    mylist = list2
        return mylist