class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max_product = INT_MIN;
        int current_product = 1;
        int n=nums.size();

        for(int i=0; i<n; i++)
        {
            current_product *= nums[i];
            if(max_product < current_product){
                max_product = current_product;
            }

            if(current_product == 0) current_product = 1;
        }
        current_product = 1;
        for(int i=n-1; i>=0; i--)
        {
            current_product *= nums[i];
            if(max_product < current_product){
                max_product = current_product;
            }
            if(current_product == 0) current_product = 1;
        }
        return max_product;
    }
};