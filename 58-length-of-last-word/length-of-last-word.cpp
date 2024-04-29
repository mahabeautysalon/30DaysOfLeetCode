class Solution {
public:
    int lengthOfLastWord(string s) {
        int count=0;
        bool check = false;
        for(int i=s.size()-1; i>=0; i--)
        {
            if(isalpha(s[i]))
            {
                check = true;
            }
            if(check)
            {
                if(s[i]==' ')
                {
                    break;
                }
                count++;
            }
            
        }
        return count;
    }
};