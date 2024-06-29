class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int maximumOperation = 0;
        int n = nums.size();
        sort(nums.begin(),nums.end());
        int start = 0,end=n-1,mid = (start+end)/2,val =0;
        for(int i=0; i<nums.size(); i++)
        {
            start=i+1,end=nums.size()-1;
            mid = (start+end)/2;
            val = k-nums[i];
            while(start<=end and nums[mid]!=val){
                if(nums[mid]<val){
                    start = mid+1;
                }else{
                    end= mid-1;
                }
                mid = (start+end)/2;
            }
            if(nums[mid] == val && i!=mid){
                maximumOperation++;
                nums.erase(nums.begin()+mid);
                nums.erase(nums.begin()+i);
                i--;
            }
        }
        
        return maximumOperation;
    }
};