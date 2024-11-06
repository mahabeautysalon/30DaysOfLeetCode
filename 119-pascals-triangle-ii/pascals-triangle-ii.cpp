class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> pre = {1,1};
        if(rowIndex == 0){
            return {1};
        }else if(rowIndex == 1){
            return {1,1};
        }
        vector<int> next;
        for(int j=1; j<rowIndex; j++){
            next.clear();
            next.push_back(1);
            for(int i=0; i<pre.size()-1; i++){
                next.push_back(pre[i]+pre[i+1]);
            }
            next.push_back(1);
            pre = next;
        }
        return next;
    }
};