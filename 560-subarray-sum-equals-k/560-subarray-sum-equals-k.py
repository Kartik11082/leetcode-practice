class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        resSum, res = 0, 0
        pfs = {0: 1}

        for n in nums:
            resSum += n
            diff = resSum - k

            res += pfs.get(diff, 0)
            pfs[resSum] = 1 + pfs.get(resSum, 0)

        return res