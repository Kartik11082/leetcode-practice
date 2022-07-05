class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s1, s2 = 0, 0
        for i in range(len(num1)):
            s1 = s1*10 + int(num1[i])
        for i in range(len(num2)):
            s2 = s2*10 + int(num2[i])

        return str(s1 + s2)