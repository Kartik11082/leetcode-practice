class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
        res = [];
        temp = "";
        for word in words:
            temp = "";
            for char in word:
                temp += morseCodes[ord(char) - 97]
            res.append(temp)
        return len(set(res))