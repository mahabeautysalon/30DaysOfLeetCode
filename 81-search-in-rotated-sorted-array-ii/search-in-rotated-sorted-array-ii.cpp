class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int n =nums.size();
        for(int i=0; i<nums.size(); i++){
            if(nums[i] == target || nums[n-i-1] == target){
                return true;
            }
            
        }
        return false;
    }
};