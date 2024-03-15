class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if(m==1&&n==0)
        {
            return;
        }else if(n==1&&m==0)
        {
            nums1[0]=nums2[0];
        }
        vector<int> temp = nums1;
        int i=0,item=0,num1_index=0,num2_index=0;
        while(num1_index<m && num2_index<n)
        {
            if(temp[num1_index]<nums2[num2_index])
            {
                nums1[i]=temp[num1_index];
                num1_index++;
            }else{
                nums1[i]=nums2[num2_index];
                num2_index++;
            }
            i++;
        }
        if(num1_index >= m)
        {
            while(i<nums1.size())
            {
                nums1[i]=nums2[num2_index];
                i++;
                num2_index++;
            }
            
        }else{
            while(i<nums1.size())
            {
                nums1[i]=temp[num1_index];
                i++;
                num1_index++;
            }
        }
    }
};