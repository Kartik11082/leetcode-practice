class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, res = 0, []
        
        if len(nums) == 0:
            return res
        
        while i < len(nums):
            start = nums[i]
            while (i != len(nums) - 1) and (nums[i+1] == nums[i]+1):
                i+=1
            if start != nums[i]:
                res.append("{}->{}".format(start, nums[i]))
            else:
                res.append(str(nums[i]))
            i+=1
        return res