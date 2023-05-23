#include <algorithm>
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int prev = 0; int max= 0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] == 1 && prev != 1 ) count = 1;
            if(1 == nums[i] && prev == 1) count = count + 1;
            
            if((nums[i] != 1 && prev == 1 )|| i == nums.size()-1){max = std::max(count, max); count = 0;}
            prev = nums[i];
        } 
        return max;
    }
};
