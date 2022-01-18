class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if (self.binarySearch(target, m)):
                return True

    def binarySearch(self, target, l):
        left, right =  0, len(l) - 1
        mid = 0

        while left <= right:
            mid = (left + right) // 2

            if target > l[mid]:
                left = mid + 1
                continue

            elif target < l[mid]:
                right = mid - 1
                continue
            return True

        return False
