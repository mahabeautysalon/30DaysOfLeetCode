class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<string> val=strs;
        vector<vector<string>> res;
        vector<string> temp;
        for(int i=0; i<strs.size(); i++)
        {
            sort(strs[i].begin(),strs[i].end());
        }
        int ptr=0;
        string text;
        while(strs.size()>0)
        {
            ptr=0;
            text = strs[0];
            while(ptr<strs.size())
            {
                //cout << strs[ptr] << " : " << val[ptr] <<" : " << text << endl;
                if(strs[ptr]==text)
                {
                    temp.push_back(val[ptr]);
                    val.erase(val.begin()+ptr);
                    strs.erase(strs.begin()+ptr);
                }else{
                    ptr++;
                }
            }
            //cout << " next array : " << endl;
            res.push_back(temp);
            temp.clear();
        }
        return res;
    }
};