class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        
        maxi = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            if boxTypes[i][0] < truckSize:
                maxi += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
        
            else:
                maxi += truckSize * boxTypes[i][1]
                truckSize = 0
            i += 1    
        
        return maxi
            