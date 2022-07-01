class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Fractional Knapsack Problem
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        totalUnits, i = 0, 0
        
        while (truckSize > 0) and (i < len(boxTypes)):
            if (boxTypes[i][0] < truckSize):
                totalUnits += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
            else:
                canTake = truckSize
                truckSize -= canTake
                totalUnits += canTake * boxTypes[i][1]
            i += 1
        return totalUnits