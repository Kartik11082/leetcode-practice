class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] += 1
        c = 0

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += c
            c = 0
            if digits[i] == 10:
                c = 1
                digits[i] = 0

        if c != 0:
        digits.insert(0, 1)

        return digits
