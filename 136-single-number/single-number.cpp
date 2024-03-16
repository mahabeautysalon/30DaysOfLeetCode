class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int count=1,unique=0;
        sort(nums.begin(),nums.end());
        if(nums.size()==1)
        {
            return nums[0];
        }else if(nums[0]!=nums[1]){
            return nums[0];
        }else{
            for(int i=0; i<nums.size(); i++)
            {
                if(nums[i]==nums[i+1])
                {
                    count++;
                }else{
                    if(count==1)
                    {
                        unique=nums[i];
                        return unique;
                    }
                    count=1;
                }
            }
        }
        return unique;
    }
};