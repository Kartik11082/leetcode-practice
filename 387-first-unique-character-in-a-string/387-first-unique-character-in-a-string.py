class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}
        for c in s:
            if c not in hm:
                hm[c] = 0
            else:
                hm[c] += 1
        
        for key, value in hm.items():
            if value == 0:
                return s.index(key)
        
        return -1