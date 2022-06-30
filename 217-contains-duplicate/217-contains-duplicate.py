class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for n in nums:
            if n in hm:
                return True
            else:
                hm[n] = 0
        return False