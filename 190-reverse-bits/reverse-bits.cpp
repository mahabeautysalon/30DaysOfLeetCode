class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t x=n;
        uint32_t res=0;
        string binary="";
        char dd;
        while(x!=0)
        {
            int q = x%2;
            x/=2;
            dd=q+48;
            binary+=dd;
        }
        int jj=31;
        for(int i=0; i<binary.size(); i++)
        {
            res+=(binary[i]-48)*pow(2,jj);
            jj--;
        }
        return res;
    }
};