class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        res = []
        
        for n in candies:
            t = extraCandies + n
            if t >= maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res