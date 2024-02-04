class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        array = []
        rem1, rem2 = [], []
        for i in set(nums1):
            if i not in set(nums2): # 1) Here: != operator doesn't work with set. 
                rem1.append(i)  #2) Both the element in the condition needs to be in set values to be compared
        
        for j in set(nums2):
            if j not in set(nums1):
                rem2.append(j)
        
        array.append(rem1)
        array.append(rem2)

        return array
                
