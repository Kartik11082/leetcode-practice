class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSECODES = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSECODES[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)