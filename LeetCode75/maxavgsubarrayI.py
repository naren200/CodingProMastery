class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        start = 0
        windowsum = 0
        max_sum = -1 * float('inf')

        if k==0:
            return 0

        for i in range(0,len(nums)):
            windowsum += nums[i]
            
            if(i-start+1==k):
                max_sum = max(windowsum, max_sum)
                windowsum -= nums[start]
                start += 1

        return float(max_sum/k)
