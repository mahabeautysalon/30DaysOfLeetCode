class Solution {
public:
    int tribonacci(int n) {
        int data[38];
        data[0] = 0,data[1]=1 , data[2] = 1;
        for(int i=3; i<=n; i++){
            data[i] = data[i-3] + data[i-2] + data[i-1];
        }
        
        return data[n];
    }
};