class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float(inf)
        globalDiff = float(inf)
        n = len(nums)
        for i in range(n):
            j, k = i+1, n-1
            while j<k:
                add=nums[i]+nums[j]+nums[k]
                localDiff=abs(target-add)    
                if localDiff==0:
                    return add
                if localDiff < globalDiff:
                    globalDiff=localDiff
                    closestSum=add
                if add<target:
                    j+=1
                elif add>target:
                    k-=1
        return closestSum