class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # array = [0]*len(nums)
        index, is_zeros = 0, 0
        for i in nums:
            if i!=0:
                nums[index] = i
                index += 1
            else:
                is_zeros += 1
            
        for i in range(is_zeros):
            nums[index] = 0
            index += 1

        # nums = array
        