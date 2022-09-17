class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        hashMap = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))
        res = []
        for i in range((len(hashMap.values())) - k):
            hashMap.popitem()
        print(hashMap)

        for i in range(len(hashMap.values())):
            res.append(hashMap.popitem()[0])
        return (res)