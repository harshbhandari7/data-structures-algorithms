class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        leng = len(intervals)
        op = []
        intervals.sort(key = lambda x: x[0])
        
        for i in range(leng):
          start, end = intervals[i]
          leng_op = len(op)
          
          if leng_op and op[-1][1] >= start:
            op[-1] = [op[-1][0], max(op[-1][1], end)]
          else:
            op.append([start, end])
        
        return op