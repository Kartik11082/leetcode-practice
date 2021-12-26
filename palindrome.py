# class Solution(object):
#     def isPalindrome(self, x):
#         a = [x for x in str(x)]
#         return a[::-1] == a
# 
# obj = Solution()
# print(obj.isPalindrome(121))

class Solution(object):
    def isPalindrome(self, x):
        return [x for x in str(x)][::-1] == [x for x in str(x)]

obj = Solution()
print(obj.isPalindrome(121))
