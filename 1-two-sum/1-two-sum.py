class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        diffDict = dict()
        for i, n in enumerate(nums):
            if (target - n) in diffDict:
                return [i, diffDict[target - n]]
            diffDict[n] = i