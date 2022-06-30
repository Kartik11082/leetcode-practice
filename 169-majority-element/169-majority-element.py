class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for n in nums:
            if count == 0:
                candidate = n
            count += (1 if n == candidate else -1)

        return candidate

#         hm = dict()
        
#         for n in nums:
#             if n in hm:
#                 hm[n] += 1
#             else:
#                 hm[n] = 1
        
#         for key, value in hm.items():
#             if (value >= (len(nums) / 2)):
#                 return key
        
#         return -1