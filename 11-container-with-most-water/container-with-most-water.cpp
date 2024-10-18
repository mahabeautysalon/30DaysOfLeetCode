int min(int a,int b){
    if(a<b){
        return a;
    }else{
        return b;
    }
}
int max(int a,int b){
    if(a<b){
        return b;
    }else{
        return a;
    }
}

class Solution {
public:
    int maxArea(vector<int>& height) {
        int beg=0,end=height.size()-1; 
        int max_area = 0,area=0;
        while(beg<end){
            area = (min(height[beg],height[end])*(end-beg));
            max_area = max(max_area,area);
            if(height[beg]<height[end]){
                beg++;
            }else{
                end--;
            }
        }
        return max_area;
    }
};