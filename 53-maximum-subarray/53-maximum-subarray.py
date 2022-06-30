class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_here = 0
        
        for n in nums:
            max_here += n
            if max_here > max_so_far:
                max_so_far = max_here
            if max_here < 0:
                max_here = 0
        return max_so_far