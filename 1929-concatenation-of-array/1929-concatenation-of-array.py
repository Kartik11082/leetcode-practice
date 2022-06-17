class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans, n = ([0] * (2*len(nums))), len(nums)
        ans[0:len(nums)] = nums[:]
        ans[(len(nums)):] = nums[:]
        return ans