class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>>res(n,vector<int>(n,0));
        int srow=0,scol=0;
        int erow=n-1,ecol=n-1;
        int val = 1;
        while(srow<=erow && scol <= ecol){
            // top
            for(int i=scol; i<=ecol; i++)
            {
                res[srow][i] = val++;
            }
            // right
            for(int i=srow+1; i<=erow; i++)
            {
                res[i][ecol] = val++;
            }
            // bottom
            for(int i=ecol-1; i>=scol; i--)
            {
                if(srow == erow){
                    break;
                }
                res[erow][i] = val++;
            }
            // left
            for(int i=erow-1; i>srow; i--)
            {
                if(scol == ecol){
                    break;
                }
                res[i][scol] = val++;
            }
            srow++;scol++;
            erow--;ecol--;
        }
        return res;
    }
};