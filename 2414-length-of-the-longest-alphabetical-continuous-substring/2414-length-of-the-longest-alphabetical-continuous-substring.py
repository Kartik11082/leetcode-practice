class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        longest = 0
        left, right = 0, 1

        if len(s) == 1:
            return 1
        
        while right < len(s):
            while  right != len(s) and (ord(s[right]) - ord(s[right - 1]) == 1):
                right += 1
            longest = max(right - left, longest)
            left = right
            right += 1
        return longest