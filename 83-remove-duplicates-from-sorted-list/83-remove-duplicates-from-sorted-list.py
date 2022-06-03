# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return
        
        unique = ListNode(head.val, head.next)
        head = unique
        tail = head.next
        
        while tail:
            if head.val != tail.val:
                head.next = tail
                head = tail
            tail = tail.next

        # For the last case of repeating number
        head.next = None
        
        return unique