class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        string temp="0";
        vector<string> res;
        bool check = true;
        int pos=0,n=words[0].size(),m=words.size();
        for(int i=0; i<n; i++)
        {
            check = true;
            temp[0]=words[0][i];
            for(int j=1; j<m; j++)
            {
                pos = words[j].find(temp);
                if(pos==string::npos)
                {
                    check = false;
                    break;
                }else{
                    words[j].erase(words[j].begin()+pos);
                }
            }
            if(check)
            {
                res.push_back(temp);
            }
        }
        return res;
    }
};