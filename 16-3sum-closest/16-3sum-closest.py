class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float(inf)
        minDiff = float(inf)
        n = len(nums)
        for i in range(n):
            j, k = i+1, n-1
            while j<k:
                add=nums[i]+nums[j]+nums[k]
                diff=abs(target-add)    
                if diff==0:
                    return add
                if diff<minDiff:
                    minDiff=diff
                    closestSum=add
                if add<target:
                    j+=1
                elif add>target:
                    k-=1
        return closestSum