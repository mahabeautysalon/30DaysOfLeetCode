class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        vector <int> pre;
        vector <int> next;
            next.push_back(1);
            res.push_back(next);
        if(numRows==1)
        {
            return res;
        }
        int sum=0;
        for(int i=1; i<numRows; i++)
        {
            int size = next.size();
            pre.assign(next.begin(),next.begin()+size);
            //copy(begin(next),end(next),back_inserter(pre));
            cout << pre.size() << endl;
            next.clear();
            next.push_back(1);
            for(int j=0; j<pre.size()-1; j++)
            {
                sum=pre[j]+pre[j+1];
                cout << sum << endl;
                next.push_back(sum);
            }
            next.push_back(1);
            res.push_back(next);
        }
        return res;
    }
};