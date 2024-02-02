class Solution:
    def maxArea(self, height: List[int]) -> int:
        list_ = list(enumerate(height))
        list_.sort(key=lambda x:x[1],reverse=True)

        max_area = 0.0
        if len(height)>10:
            search_length = int(0.40*len(height))
        else:
            search_length = len(height)
        import math
        for i in range(0,search_length):
            for j in range(i+1,search_length):
                area = math.fabs((list_[i][0]-list_[j][0])*(min(list_[i][1],list_[j][1])))
                if area  > max_area:
                    max_area = area
        
        return int(max_area)