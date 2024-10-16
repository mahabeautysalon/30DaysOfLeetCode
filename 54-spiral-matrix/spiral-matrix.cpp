class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int srow=0,scol=0;
        int erow=matrix.size()-1,ecol = matrix[0].size()-1;
        vector<int> res;
        while(srow<=erow && scol <=ecol){
            // top
            for(int i=scol; i<=ecol; i++)
            {
                //cout << matrix[srow][i] << " ";
                res.push_back(matrix[srow][i]);
            }
           // cout << endl;
            // right
            for(int i=srow+1; i<=erow; i++)
            {
                //cout << matrix[i][ecol] << " ";
                res.push_back(matrix[i][ecol]);
            }
           // cout << endl;
            // bottom
            for(int i=ecol-1; i>=scol; i--)
            {
                if(srow == erow){
                    break;
                }
               // cout << matrix[erow][i] << " ";
                res.push_back(matrix[erow][i]);
            }
            //cout << endl;
            // left
            for(int i=erow-1; i>srow; i--)
            {
                if(scol == ecol){
                    break;
                }
                //cout << matrix[i][scol] << " ";
                res.push_back(matrix[i][scol]);
            }
            //cout << endl;
            srow++;scol++;
            erow--;ecol--;
        }
        return res;
        
    }
};