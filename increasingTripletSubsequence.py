class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = float("inf"), float("inf")

        if len(nums) < 3:
            return False

        for n in nums:
            if n <= i:
                i = n
            elif n <= j:
                j = n
            else:
                return True
        return False
