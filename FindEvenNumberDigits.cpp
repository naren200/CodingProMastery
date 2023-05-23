#include <string>
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int len;
        int cnt=0;
        for(int i=0; i<nums.size(); i++){
            len = std::to_string(nums[i]).length();
            if(len%2==0)cnt = cnt + 1;
        }
        return cnt;
    }
    
};
