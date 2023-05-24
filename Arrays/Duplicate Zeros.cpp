class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int pt_sz = arr.size();
        vector<int> se(pt_sz);
        int tk = 0;
        
        for (int i=0; i<arr.size(); i++){
            if(pt_sz==1)break;
            if(tk>=pt_sz)break;
            cout<<tk<<endl;
            if(arr[i]==0){
                se[tk] = 0;
                if(tk<=pt_sz-2)se[tk+1] = 0;
                tk = tk+2;
            }
            else if(arr[i]!=0){
                se[tk] = arr[i];
                tk++;
            }
        }
        arr = se;
    }
};

//Runtime: 23 ms
//Memory Usage: 9.7 MB
// Learnings: 
// Takeaways: 