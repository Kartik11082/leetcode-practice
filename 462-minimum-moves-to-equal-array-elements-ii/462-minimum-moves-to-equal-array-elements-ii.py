class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        midValue = nums[n//2]
        opCount = 0
        
        for n in nums:
            if n != midValue:
                opCount += abs(midValue - n)
        
        return opCount