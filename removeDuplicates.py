class Solution(object):
    def removeDuplicates(self, nums):
        i, j = 0, 0
        while (i != len(nums)) and (j != len(nums)):
            if (nums[i] == nums[j]):
                j += 1
            else:
                i += 1
                nums[i] = nums[j]

        i += 1
        while i < len(nums):
            nums[i] = "_"
            i += 1

        k = 0
        for n in nums:
            if n != "_":
                k += 1
        return k
