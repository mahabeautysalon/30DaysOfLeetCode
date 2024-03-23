class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for(int i=0; i<s.size(); i++)
        {
            if(s[i]=='('||s[i]=='{'||s[i]=='[')
            {
                stack.push_back(s[i]);
            }else if(stack.size()!=0)
            {
                if((s[i]==')'&&stack[stack.size()-1]=='(')||(s[i]=='}'&&stack[stack.size()-1]=='{')||(s[i]==']'&& stack[stack.size()-1]=='['))
                {
                    stack.pop_back();
                }else{
                    return false;
                }
            }else{
                return false;
            }
        }
        if(stack.size()==0)
        {
            return true;
        }else{
            return false;
        }
        
    }
};