class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = sorted(boxTypes, key=lambda box: box[1], reverse=True)
        
        maxi = 0
        i = 0
        while truckSize > 0 and i < len(boxes):
            if boxes[i][0] < truckSize:
                maxi += boxes[i][0] * boxes[i][1]
                truckSize -= boxes[i][0]
        
            else:
                maxi += truckSize * boxes[i][1]
                truckSize = 0
            i += 1    
        
        return maxi
            