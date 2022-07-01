class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        revWords = ''
        for word in words[::-1]:
            revWords += (word + " ")
        return revWords[:-1]