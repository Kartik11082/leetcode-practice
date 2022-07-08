class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum_arr={}
        length = len(nums)
            
        for i in range(len(nums)-2):
            left = i+1
            right = length-1
            while left<right:
                total_sum = nums[i]+nums[left]+nums[right]
                diff = total_sum - target
                if diff < 0:
                    left+=1
                    sum_arr[total_sum] = diff
                elif diff>0:
                    right-=1
                    sum_arr[total_sum] = diff
                else:
                    return total_sum
        return min(sum_arr, key=lambda x:abs(sum_arr[x]))