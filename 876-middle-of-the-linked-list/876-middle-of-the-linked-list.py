# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        length = self.getLength(head)
        if length % 2 == 0:
            mid = (length // 2)
        else:
            mid = (length // 2)
        
        curr = head
        for i in range(mid):
            curr = curr.next
        
        return curr
        
        
    def getLength(self, curr):
        count = 0
        while curr != None:
            count += 1
            curr = curr.next
        return count
        
        # p1 = p2 = head
        # while p2 and p2.next:
        #     p1 = p1.next
        #     p2 = p2.next.next
        # return p1