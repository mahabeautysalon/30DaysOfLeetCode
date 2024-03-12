class Solution {
public:
    bool isPalindrome(int x) {
        int n=x;
        unsigned long long int palindrome_no = 0;
        while(x>0)
        {
            int q = x%10;
            x/=10;
            palindrome_no = palindrome_no*10+q;
        }
        if(n == palindrome_no)
        {
            return true;
        }
        return false;
    }
};