# O(n^2) Solution
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i, _ in enumerate(nums):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return i, j
# 
# obj = Solution()
# print(obj.twoSum([3, 2, 4], 6))

# O(n) Solution
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            print(hashmap)
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

obj = Solution()
print(obj.twoSum([3, 1, 4, 4, 2], 6))
