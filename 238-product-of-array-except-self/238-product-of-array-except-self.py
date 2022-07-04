class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        # Prefix Array
        p = 1
        for i in range(len(nums)):
            res[i] = p
            p *= nums[i]

        # Postfix Array
        p = 1
        for i in range((len(nums) - 1), -1, -1):
            res[i] *= p
            p *= nums[i]

        return res