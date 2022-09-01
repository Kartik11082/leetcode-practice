class Solution:
    def isHappy(self, n: int) -> bool:
        def getSumOfSquares(num):
            sum = 0;
            for n in str(num):
                sum += (int(n)) ** 2
            return sum

        visited = set()
        while getSumOfSquares(n) not in visited:
            if getSumOfSquares(n) == 1:
                return True
            visited.add(getSumOfSquares(n))
            n = getSumOfSquares(n)
        return False