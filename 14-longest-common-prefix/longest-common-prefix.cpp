class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res="";
        if(strs[0]=="")
        {
            return res;
        }
        
        bool check = true;
        for(int i=0; i<strs[0].size(); i++)
        {
            check = true;
            for(int j=0; j<strs.size(); j++)
            {
                if(strs[0][i]!=strs[j][i])
                {
                    check = false;
                    return res;
                }
            }
            if(check)
            {
                res+=strs[0][i];
            }
        }
        return res;
    }
};