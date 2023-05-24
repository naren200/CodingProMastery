class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> squr(nums.size());
        for (int i = 0; i<nums.size(); i++){
            squr[i] = nums[i]*nums[i];
        }
        sort(squr.begin(), squr.end());
        return squr;
    }
};

//Runtime: 44 ms
//Memory Usage: 25.9 MB
// Learnings:
// Takeaways: