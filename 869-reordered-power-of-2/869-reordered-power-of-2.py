class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c = Counter([int(i) for i in str(n)])
        
        n, i = 0, 0
        while n <= 10**9:
            n = 2**i
            d = Counter([int(i) for i in str(n)])
            print(d, " : ", c)
            if c == d:
                return True
            i += 1
        return False