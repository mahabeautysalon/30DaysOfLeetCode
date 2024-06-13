class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        string temp="0";
        vector<string> res;
        bool check = true;
        int pos=0;
        for(int i=0; i<words[0].size(); i++)
        {
            check = true;
            temp[0]=words[0][i];
            for(int j=1; j<words.size(); j++)
            {
                cout << "pos : " << words[j].find(temp) << endl;
                if(words[j].find(temp)==string::npos)
                {
                    check = false;
                    break;
                }else{
                    pos = words[j].find(temp);
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