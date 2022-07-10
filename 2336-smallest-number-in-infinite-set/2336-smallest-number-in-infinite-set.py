class SmallestInfiniteSet:

    def __init__(self):
      lst = list(range(1, 1001))
      self.nums = deque(lst)

    def popSmallest(self) -> int:
      temp = sorted(self.nums)
      ele = temp[0]
      self.nums.remove(ele)
      return ele

    def addBack(self, num: int) -> None:
      if num not in self.nums:
        self.nums.append(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)