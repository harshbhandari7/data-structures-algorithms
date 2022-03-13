class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        leng = len(intervals)
        if (leng == 1):
            return intervals
        intervals = sorted(intervals, key=lambda i: i[0])
        out = []
        for interval in intervals:
            if len(out) and (out[-1][1] >= interval[0]):
                out[-1] = [out[-1][0], max(out[-1][1], interval[1])]
            else:
                out.append(interval)
        return out