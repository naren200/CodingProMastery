// https://leetcode.com/explore/featured/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> nums1_copy = nums1;
        int i = 0;
        int j = 0;
        
        for(int k=0; k<m+n; k++)
        {
            // What if the arrays are null
            if(n==0){
                break;
            }
            if(m==0){
                nums1 = nums2;
                break;
            }
            
            // TO make sure the index of two iterations i and j doesn't go off limits
            if(j==n){
                j=n-1;
                nums2[j] = INT_MAX;
            }
            if(i==m){
                i = m-1;
                nums1_copy[i] = INT_MAX;
            }
            
           
            // To iterate through each element 
            if(nums1_copy[i]<nums2[j] && i<m){
                cout<<"i = " << i;
                nums1[k] = nums1_copy[i];
                i++;
                // if(i==m-1) nums1_copy[i]=INT_MAX;
                
            }
            else {
                cout<<"j = "<< j;
                nums1[k] = nums2[j];
                // if(j<n-1)
                j++;
                // if(j==n-1) nums2[j] = INT_MAX;
            }
        }
    }
};
