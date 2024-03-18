class Solution {
public:
    int getSum(int a, int b) {
        unsigned int num1,num2,i=0;
        if(a<b)
        {
            num1=a;
            num2=b;
        }else{
            num1=b;
            num2=a;
        }
        while(i!=num1)
        {
            ++num2;
            i++;
        }
        return num2;
    }
};