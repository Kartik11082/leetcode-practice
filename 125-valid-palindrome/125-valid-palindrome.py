class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""

        if s == " ":
            return True

        for c in s:
            if c.isalnum():
                r += c
        return r.lower() == r[::-1].lower()