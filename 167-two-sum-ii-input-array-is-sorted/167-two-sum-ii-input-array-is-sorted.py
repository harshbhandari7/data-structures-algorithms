class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two sum using 2 pointer technique
        leng = len(numbers)
        start = 0
        end = leng - 1
        while (start <= end):
            if (numbers[start] + numbers[end] == target):
                return [ start+1, end+1 ]
            elif (target < (numbers[start] + numbers[end])):
                end -= 1
            else:
                start += 1