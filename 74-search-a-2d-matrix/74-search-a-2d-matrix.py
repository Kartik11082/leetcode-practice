class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        l, r = 0, M*N - 1
        
        while l<=r:
            mid = (l+r)//2
            
            # we found target
            if matrix[mid//N][mid%N] == target: return True
            
            # target must be on the right side of mid
            if matrix[mid//N][mid%N] < target: l = mid + 1
            
            # target must be on the left side of mid
            else: r = mid - 1
            
# we are out of the while loop which means the element is not in the matrix so we return false
        return False