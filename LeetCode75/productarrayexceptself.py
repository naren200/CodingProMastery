class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_exists = False
        second_zero_exists = False
        for i in nums:
            if i!= 0:
                product *= i
            else:
                if zero_exists == True and i == 0:
                    second_zero_exists = True
                zero_exists = True
        answers = [1]*len(nums)
        for i in range(0,len(nums),1):
            if second_zero_exists == True:
                return [0]*len(nums)
            if zero_exists == True:
                answers = [0]*len(nums)
                if nums[i]==0:
                    answers[i] = product 
                    return answers
            if nums[i]!=0:
                answers[i] = int(product/nums[i])

        return answers
