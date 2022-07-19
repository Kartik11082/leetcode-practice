class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # diffDict = dict()
        # for i, n in enumerate(nums):
        #     if (target - n) in diffDict:
        #         return [i, diffDict[target - n]]
        #     diffDict[n] = i
        
        d = {}
        # Loop through the list
        for i in range(len(nums)):
            # Check if the difference is in the dictionary
            if target - nums[i] in d:
                # Return the index of the value
                return [d[target - nums[i]], i]
            # Add the value to the dictionary
            d[nums[i]] = i
        # Return None if the value is not in the dictionary
        return None