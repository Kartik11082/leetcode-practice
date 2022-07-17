class Solution:
    def minPartitions(self, n: str) -> int:
        nList = list(map(int, list(n)))
        return (max(nList))