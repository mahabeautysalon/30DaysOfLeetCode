class Solution {
public:
    void printQ(vector<string> q){
        int n= q.size();
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                cout << q[i][j] << " ";
            }
            cout << endl;
        }
    }
    bool isSafe(vector<string>q, int row, int col){
        int n = q.size();
        // column 
        for(int i=0; i<row; i++){
            if(q[i][col] == 'Q'){
                return false;
            }
        }
        
        // left DIagonal
        int i=row-1,j = col-1;
        while(i>=0 && j>=0){
            if(q[i][j] == 'Q'){
                return false;
            }
            i--;j--;
        }

        // right DIagonal
        i = row-1, j = col +1;
        while(i>=0 && j<n){
            if(q[i][j] == 'Q'){
                return false;
            }
            i--;j++;
        }

        return true;
    }
    
    void queens(vector<string> q, int row,vector<vector<string>>&ans ){
        int n = q.size();
        if(row == n){
            ans.push_back(q);
            return;
        }
        for(int i=0; i<n; i++){
            if(isSafe(q, row, i)){
                q[row][i] = 'Q';
                queens(q, row+1,ans);
                q[row][i] = '.';
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<string> q(n,string(n, '.'));
        vector<vector<string>> ans;
        queens(q,0,ans);
        return ans;
    }
};