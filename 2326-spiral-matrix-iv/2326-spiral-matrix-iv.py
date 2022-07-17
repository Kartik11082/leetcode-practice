# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        left, right = 0, n
        top, bottom = 0, m
        resList = [[-1 for x in range(n)] for y in range(m)] 
        node = head
        
        while left <= right and top <= bottom:
            for i in range(left, right):
                if node:
                    resList[top][i] = node.val
                    node = node.next
            top += 1
            
            for j in range(top, bottom):
                if node:
                    resList[j][right-1] = node.val
                    node = node.next
            right -= 1

            for k in reversed(range(left, right)):
                if node:
                    resList[bottom-1][k] = node.val
                    node = node.next
            bottom -= 1
            
            for l in reversed(range(top, bottom)):
                if node:
                    resList[l][left] = node.val
                    node = node.next
            left += 1
        
        return resList