class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double res=3.5;
        
        for(int i=0; i<nums2.size(); i++)
        {
            nums1.insert(upper_bound(nums1.begin(),nums1.end(),nums2[i]),nums2[i]);
        }
        if(nums1.size()==1)
        {
            return nums1[0];
        }
        int mid=(nums1.size()/2);
        double x=nums1[mid-1],y=nums1[mid];
        if(nums1.size()%2==0)
        {
            res = ((x+y)/2.00);
        }else{
            
            res=y;
        }
        return res;
    }
};