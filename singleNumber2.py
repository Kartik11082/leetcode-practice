class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for i in range(32):
            count = 0
            for n in nums:
                bit = n >> i
                bit &= 1
                count += bit
                rem = count % 3

                if i == 31 and rem:  # must handle the negative case
                    res -= 1 << 31
                else:
                    res |= rem << i

        return res
