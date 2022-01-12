class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = dict()

        for n in nums:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 1
        for key, value in hm.items():
            if (value >= (len(nums) / 2)):
                return key

        return -1
