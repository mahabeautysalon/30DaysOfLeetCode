class Solution {
public:
    bool isPerfectSquare(unsigned long long int num) {
        if(num<=1)
        {
            return true;
        }
        for(unsigned long long int i=2; i<num+2/2; i++)
        {
            if(i*i==num)
            {
                cout << i << " " << i*i;
                return true;
            }
        }
        return false;
    }
};