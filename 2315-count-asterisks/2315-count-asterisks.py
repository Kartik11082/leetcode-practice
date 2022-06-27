class Solution:
    def countAsterisks(self, s: str) -> int:
        lineCount = astCount = 0
        for c in s:
            if c == "|":
                lineCount += 1
            if lineCount % 2 == 0:
                if c == "*":
                    astCount += 1
        return astCount