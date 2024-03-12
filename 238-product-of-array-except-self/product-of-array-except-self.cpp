class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> pro;
        long long int product=1;
        int temp=0;
        for(int i=0; i<nums.size(); i++)
        {
            product*=nums[i];
        }
        for(int i=0; i<nums.size(); i++)
        {
            if(nums[i]!=0)
            {
                temp=product/nums[i];
            }else{
                temp=1;
                for(int j=0; j<nums.size(); j++)
                {
                    if(i!=j)
                    {
                        temp*=nums[j];
                    }
                }
            }
            
            pro.push_back(temp);
        }
        return pro;
    }
};