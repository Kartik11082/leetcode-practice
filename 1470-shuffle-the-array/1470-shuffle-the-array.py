class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:len(nums) // 2]
        nums2 = nums[len(nums) // 2:]
        res = []
        for n1, n2 in zip(nums1, nums2):
            res.append(n1)
            res.append(n2)
        return res