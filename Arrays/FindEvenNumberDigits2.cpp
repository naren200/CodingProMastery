#include <string>
class Solution {
private:
    int getNumberDigit(int n){
        int digt=1;
        while (true)
        {
            if(n/10 != 0){
                n = n/10;
                digt = digt + 1;
            }
            else{
                break;
            }
        }
        return digt;
    }
public:
    int findNumbers(vector<int>& nums) {
        int len;
        int cnt=0;
        for(int i=0; i<nums.size(); i++){
            if(getNumberDigit(nums[i])%2==0)cnt = cnt + 1;
        }
        return cnt;
    }
    
};

//Runtime: 0 ms
//Memory Usage: 9.8 MB
// Learnings: If the String library is called then the runtime is increased even though there is 
// no functions are called using string.
// Conclusion: Remove unecessary library call definitions in a program to reduce run time.