class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        elif len(strs) == 1:
            return [strs]

        sStrs = []
        hashMap = {}
        for word in strs:
            key = "".join(sorted(word))
            value = word
            if key in hashMap:
                hashMap[key].append(value)
            elif key not in hashMap:
                hashMap[key] = [value]
                
        res = []
        for value in hashMap.values():
            res.append(value)
        return res