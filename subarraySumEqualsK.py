class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum, res = 0, 0
        pfs = {0: 1}

        for n in nums:
            sum += n
            diff = sum - k

            res += pfs.get(diff, 0)
            pfs[sum] = 1 + pfs.get(sum, 0)

        return res