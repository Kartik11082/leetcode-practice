class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        count = 0
        firstInterval = intervals[0]

        for i in range(1, len(intervals)):
            secondInterval = intervals[i]
            start1, end1 = firstInterval[0], firstInterval[1]
            start2, end2 = secondInterval[0], secondInterval[1]

            if start1 < end2 and start2 < end1:
                count += 1
            else:
                firstInterval = secondInterval

        return count
