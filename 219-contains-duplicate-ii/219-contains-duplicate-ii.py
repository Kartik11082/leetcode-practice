class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        for i in range(len(nums)):
            current = nums[i]
            if (current in hm) and (i - hm[current] <= k):
                return True
            else:
                hm[current] = i
        
        return False