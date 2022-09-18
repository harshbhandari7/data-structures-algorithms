class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        leng = len(intervals)
        if leng == 1:
          return intervals
        
        res = []
        intervals.sort(key=lambda x: x[0])
        for inv in intervals:
          if len(res) and res[-1][1] >= inv[0]:
            res[-1] = [res[-1][0], max(inv[1], res[-1][1])]
          else:
            res.append(inv)
        
        return res