class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}
        for c in s:
            if c not in hm:
                hm[c] = 0
            else:
                hm[c] += 1
        
        for k, v in hm.items():
            if v == 0:
                return s.index(k)
        
        return -1