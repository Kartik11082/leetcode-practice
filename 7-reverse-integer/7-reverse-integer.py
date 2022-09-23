class Solution:
    def reverse(self, x: int) -> int:
        digit, num, res = 0, abs(x), 0
        minInt, maxInt = -2**31, 2**31

        while num > 0:
            digit = num % 10
            num //= 10
            res  = res * 10 + digit
        
        if res < minInt or res > maxInt:
            return (0)
        if x < 0:
            return ((-1)*res)
        return res