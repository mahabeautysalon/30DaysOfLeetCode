class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n=nums.size(); 
        vector<int> ans;
        vector<bool> temp(n+1, false);
        for(int i=0; i<n; i++){
            if(temp[nums[i]] == false){
                temp[nums[i]] = true;
            }else{
                ans.push_back(nums[i]);
            }
            
        }
        int size = temp.size();
        for(int i=1; i<size; i++){
            if(temp[i] == false){
                ans.push_back(i);
            }
        }
        
        return ans;
    }
    
};