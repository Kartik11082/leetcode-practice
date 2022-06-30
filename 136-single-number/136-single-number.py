class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorNum = 0

        for n in nums:
            xorNum ^= n

        return xorNum

#         hashMap = dict()
        
#         for n in nums:
#             if n in hashMap:
#                 hashMap[n] += 1
#             else:
#                 hashMap[n] = 1
        
#         for key, value in hashMap.items():
#             if value == 1:
#                 return key
        
#         return -1