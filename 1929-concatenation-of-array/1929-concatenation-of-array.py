class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans, n = ([0] * (2*len(nums))), len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[n + i] = nums[i]
        return ans