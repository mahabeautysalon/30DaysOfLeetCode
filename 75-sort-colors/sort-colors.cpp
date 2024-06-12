class Solution {
public:
    void sortColors(vector<int>& nums) {
        if(nums.size()==1)
        {
            return;
        }
        vector<int> val(3,0);
        int n=nums.size();
        for(int i=0; i<n; i++)
        {
            val[nums[i]] +=1;
        }
        int index=0;
        for(int i=0; i<n; i++)
        {
            if(val[index]==0)
            {
                index++;
                if(val[index]==0)
                {
                    index++;
                }
            }
            nums[i] = index;
            val[index]-=1;
        }
    }
};