class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_cons = 0
        cons = 0 
        ahead = 0
        current_zeros = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cons += 1

            if nums[i] == 0:
                if current_zeros < k:
                    cons += 1
                else:
                    if k==0:
                        if ahead > i:
                            continue
                        else:
                            for pointer in range(i,len(nums)):
                                if nums[pointer] == 1:
                                    current_zeros = 0
                                    start = pointer
                                    ahead = start
                                    cons = 0
                                    break
                    elif k!=0:
                        cons += 1
                        for pointer in range(start,i):
                            if nums[pointer] == 0:
                                current_zeros -=1
                                cons -= 1
                                start = pointer
                                start += 1
                                break
                            else:
                                cons -= 1   

                        
                current_zeros += 1
            max_cons = max(max_cons, cons)
        
        return max_cons