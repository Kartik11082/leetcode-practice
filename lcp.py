# O(n) Solution
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         prefix = strs[0]
#         for i in range(1, (len(strs))):
#             while(strs[i].startswith(prefix) == False):
#                 prefix = prefix[0:-1]
#         return prefix
# 
# obj = Solution()
# print(obj.longestCommonPrefix(['flower', 'flow', 'flights']))

# Pythonic Solution
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for s in strs:
            while(not (s.startswith(prefix))):
                prefix = prefix[0:-1]
        return prefix

obj = Solution()
print(obj.longestCommonPrefix(['flower', 'flow', 'flights']))
