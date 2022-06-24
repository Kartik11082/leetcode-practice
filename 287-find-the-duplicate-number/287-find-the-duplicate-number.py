class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = {}
        for n in nums:
            if n in hm:
                return n
            else:
                hm[n] = 1