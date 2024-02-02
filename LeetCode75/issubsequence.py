class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        index = 0
        if(s==""):
            return True
        for i in t_list:
            if(index==len(s_list)):
                return True

            if(i==s_list[index]):
                index += 1
            else:
                continue
        if(index==len(s_list)):
            return True
  
        if(index+1!=len(s_list)):
            return False