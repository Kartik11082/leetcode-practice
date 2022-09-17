class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        elif len(strs) == 1:
            return [strs]

        hashMap = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in hashMap:
                hashMap[key].append(word)
            elif key not in hashMap:
                hashMap[key] = [word]
                
        res = []
        for value in hashMap.values():
            res.append(value)
        return res