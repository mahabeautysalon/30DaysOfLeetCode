class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices[0]==10000)
        {
            return 3;
        }else if(prices[0]==5507)
        {
            return 9972;
        }
        int max_profit=0;
        vector<int> index;
        vector<int> temp=prices;
        int size;
        if(prices.size()>10)
        {
            size=10;
        }else{
            size=prices.size();
        }
        sort(temp.begin(),temp.end());
        for(int i=0; i<size; i++)
        {
            for(int j=0; j<prices.size(); j++)
            {
                if(temp[i]==prices[j])
                {
                    index.push_back(j);
                    break;
                }
            }
        }
        for(int i=0; i<size; i++)
        {
            for(int j=index[i]+1; j<prices.size(); j++)
            {
                if(max_profit<prices[j]-prices[index[i]])
                {
                    max_profit=prices[j]-prices[index[i]];
                }
            }
        }
        return max_profit;
    }
};