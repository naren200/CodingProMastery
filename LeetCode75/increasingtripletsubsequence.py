class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        for i in range(0,len(nums)):
            for j in range(len(nums)-1, i+1, -1):
                if nums[i]>nums[j]:
                    # print("Cotin with value_i and value_j as ", nums[i] ,"  ",  nums[j])
                    continue
                
                if nums[i]<nums[j]:
                    min_val = min(nums[i+1:j])
                    max_val = max(nums[i+1:j])
                    # print(nums[i])
                    # print(min_val)
                    # print(nums[j], "\n")
                    if nums[i]<min_val and min_val<nums[j]:
                        return True
                    if nums[i]<max_val and max_val<nums[j]:
                        return True
                    else:
                        for k in range(i+1,j):
                            if nums[i]<nums[k] and nums[k]<nums[j]:
                                return True
        return False

        
