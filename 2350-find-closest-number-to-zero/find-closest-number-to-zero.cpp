class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int minDisIndex = 0;
        int n = nums.size();
        for(int i=1; i<n; i++)
        {
            if(abs(nums[i]) < abs(nums[minDisIndex])){
                minDisIndex = i;
            }else if(abs(nums[i]) == abs(nums[minDisIndex])){
                if(nums[i]>nums[minDisIndex]){
                    minDisIndex = i;
                }
            }
        }
        return nums[minDisIndex];
    }
};