class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int beg=0,end=nums.size()-1,mid = (beg+end)/2;
        while(beg<=end)
        {
            //cout << "mid : " << mid << endl;
            if(target == nums[mid])
            {
                return mid;
            }
            else if(target>nums[mid])
            {
                beg = mid+1;
            }else{
                end = mid-1;
            }
            mid = (beg+end)/2;
        }
        if(nums[mid]<target)
        {
            return mid+1;
        }
        return mid;
    }
};