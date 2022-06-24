# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head
        while(p2 != None) and (p2.next != None) and (p2.next.next != None):
            p1 = p1.next
            p2 = (p2.next).next
        if p2.next and p2.next.next == None:
            return p1.next
        else:
            return p1