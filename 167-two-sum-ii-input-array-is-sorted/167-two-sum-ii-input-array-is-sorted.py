class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        while start < end:
          summ = numbers[start] + numbers[end]
          if summ == target:
            return [start + 1, end + 1]
          elif summ > target:
            end -= 1
          else:
            start += 1
    