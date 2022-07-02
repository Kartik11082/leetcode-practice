class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=0
        n=len(arr)
        for i in range(n):
            res = 0
            for j in range(i, n):
                res += arr[j]
                if ((i+j)%2==0):
                    ans=ans+res
        return ans