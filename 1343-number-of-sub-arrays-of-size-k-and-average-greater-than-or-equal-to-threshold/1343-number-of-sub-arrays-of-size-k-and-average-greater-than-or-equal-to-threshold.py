class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        leng = len(arr)
        
        n = 0
        curr_sum = 0
        
        curr_sum += sum(arr[:k])
        
        if ((curr_sum // k) >= threshold):
            n += 1
        
        for i in range(1, leng-k+1):
            curr_sum = curr_sum - arr[i-1]
            curr_sum = curr_sum + arr[i+k-1]
            
            if ((curr_sum // k) >= threshold):
                n += 1
            
            
        return n