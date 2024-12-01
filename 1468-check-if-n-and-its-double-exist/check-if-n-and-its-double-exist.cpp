class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        map<int,int>mp;
        for(int i=0; i<arr.size(); i++){
            if(mp.find(arr[i]) != mp.end()){
                return true;
            }
            if(arr[i]%2 == 0){
                mp[arr[i]/2] = true;
            }
            mp[arr[i]*2] = true;
        }
        return false;
    }
};