# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        if not list1 and not list2:
            return ListNode(0).next
        
        if not list1:
            return list2
        
        if not list2:
            return list1

        result = ListNode()
        head = result
        
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1:
            head.next = list1
        elif list2:
            head.next = list2

        return result.next