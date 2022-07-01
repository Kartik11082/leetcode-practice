class Solution:
    def reverse(self, x: int) -> int:
        digit, num, res = 0, abs(x), 0
        
        while num > 0:
            digit = num % 10
            num //= 10
            res  = res * 10 + digit
        
        if res < -2**31 or res > 2**31:
            return (0)
        if x < 0:
            return ((-1)*res)
        return res