class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOf = {}
        for c in s:
            if c not in lastOf:
                lastOf[c] = s.rindex(c)
        
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastOf[c])
            if end == i:
                res.append(size)
                size = 0
        return res