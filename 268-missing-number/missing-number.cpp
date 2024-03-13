class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int missing=-1;
        sort(nums.begin(),nums.end());
        for(int i=0; i<nums.size(); i++)
        {
            if(nums[i]!=i)
            {
                missing=i;
                break;
            }
        }
        if(missing==-1)
        {
            missing=nums.size();
        }
        return missing;
    }
};