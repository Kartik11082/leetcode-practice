class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binaryString = ""
        modulo = 10**9 + 7
        for i in range(1, n+1):
            binaryString += str(bin(i)[2:])
        return (int(binaryString, 2) % modulo)