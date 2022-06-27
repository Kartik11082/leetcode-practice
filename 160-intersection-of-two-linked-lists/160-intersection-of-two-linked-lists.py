# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        lA, lB = self.getLength(headA), self.getLength(headB)
        diff = abs(lA - lB)
        
        if lA == 1 and lB == 1:
            if pA.val == pB.val:
                return pA

        if lB > lA:
            while pB.next != None and diff:
                pB = pB.next
                diff -= 1
        elif lA > lB:
            while pA.next != None and diff:
                pA = pA.next
                diff -= 1
        
        while pA and pB:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
        return None
            

    def getLength(self, node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count