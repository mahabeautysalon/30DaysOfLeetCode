#include <bit>

class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        // check array is sorted or not
        bool check = true;
        for(int i=0; i<nums.size()-1; i++){
            if(nums[i] > nums[i+1]){
                check = false;
                break;
            }
        }

        // if array is sorted 
        if(check){
            return true;
        }

        vector<int> temp;

        // if not sorted check no of bits
        for(int i=0; i<nums.size(); i++){
            int count = 0;
            int item = nums[i];
            while(item>0){
                item = item & (item-1);
                count++;
            }
            temp.push_back(count);
            
        }

        
        int preCount = temp[0],maxValue=nums[0],totalMax=0;
        for(int i=0; i<temp.size()-1; i++){
            //cout << temp[i] << " : " << nums[i] << " and " << temp[i+1] << " : " << nums[i+1] << endl;
            if(temp[i] == temp[i+1]){
                if(nums[i+1] > maxValue){
                    maxValue = nums[i+1];
                }
                
                if(check && totalMax > nums[i+1]){
                    return false;
                }
                
                
            }else{
                //preCount = temp[i];
                check = true;
                if(maxValue > nums[i+1]){
                    return false;
                }else{
                    totalMax = maxValue;
                    maxValue = nums[i+1];
                }
            }
        }
        

        return true;
    }
};