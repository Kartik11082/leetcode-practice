class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hm = defaultdict()
        words = s.split(" ")

        if len(words)!=len(pattern) or len(set(pattern))!=len(set(words)):
            return False

        for i, val in enumerate(pattern):
            if val in hm:
                if hm[val] != words[i]:
                    return False
            else:
                hm[val] = words[i]

        return True
