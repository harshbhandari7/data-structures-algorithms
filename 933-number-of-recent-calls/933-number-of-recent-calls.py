class RecentCounter:

    def __init__(self):
        self.time_values = []
        
    def ping(self, t: int) -> int:
        while self.time_values and self.time_values[0] + 3000 < t:
            self.time_values.pop(0)
        
        self.time_values.append(t)
        
        return len(self.time_values)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)