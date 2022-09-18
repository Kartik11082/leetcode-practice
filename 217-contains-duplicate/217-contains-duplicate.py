class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = set()
        for num in nums:
            if num in hm:
                return True
            else:
                hm.add(num)
        return False