class Solution {
public:
    int findMin(vector<int>& nums) {
        int min=0;
        for(int i=0; i<nums.size(); i++)
        {
            if(nums[i]<nums[min])
            {
                min=i;
            }
        }
        return nums[min];
    }
};