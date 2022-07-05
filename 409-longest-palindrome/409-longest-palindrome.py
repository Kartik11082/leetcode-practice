class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = {}
        
        for i in s:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1

        if len(hm) == 1:
            return hm[s[0]]

        c, oddCount = 0, 0
        for v in hm.values():
            if v > 1:
                if v % 2 == 0:
                    c += v
                else:
                    c += v - 1
                    oddCount += 1
            else:
                oddCount += 1
        if oddCount > 0:
            c += 1
        
        return c