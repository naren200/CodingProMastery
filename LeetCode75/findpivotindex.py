class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left,right = nums, nums[::-1]
        rev = nums[::-1]
        for i in range(1,len(nums)):
            left[i] = left[i-1] + nums[i]
        for j in range(1,len(nums)):
            right[j] = right[j-1] + rev[j]
        right = right[::-1]
        
        
        for i in range(0,len(nums)):
            if i == 0:
                if len(right) == 1:
                    return 0
                if right[i+1] == 0:
                    return 0
                else:
                    continue
            if i==len(nums)-1:
                if 0 == left[i-1]:
                    return i
                else:
                    continue
            if left[i-1] == right[i+1]:
                return i
            


        return -1