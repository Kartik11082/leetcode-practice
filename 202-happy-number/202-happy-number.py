class Solution:
    def isHappy(self, n: int) -> bool:
        def getSumOfSquares(num):
            sum = 0;
            for n in str(num):
                sum += (int(n)) ** 2
            return sum
        numList = []
        while getSumOfSquares(n) not in numList:
            if getSumOfSquares(n) == 1:
                return True
            numList.append(getSumOfSquares(n))
            n = getSumOfSquares(n)
        return False