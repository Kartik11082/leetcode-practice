class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans, nums2 = [None] * len(nums), nums
        for i, n in list(enumerate(nums2)):
            ans[i] = nums[n]
        return ans