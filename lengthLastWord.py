class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splittedWord = s.rstrip().split(" ")
        return len(splittedWord[len(splittedWord) - 1])
