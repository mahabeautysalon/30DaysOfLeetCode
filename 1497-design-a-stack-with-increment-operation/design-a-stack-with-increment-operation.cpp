class CustomStack {
    int maximumSize=0;
    int top=-1;
    vector<int> stackData;
public:
    CustomStack(int maxSize) {
        maximumSize = maxSize;
    }
    
    void push(int x) {
        //cout << "max size : " << maximumSize << endl;
        //cout << "top : " << top << endl;
        if(top+1 < maximumSize)
        {
            stackData.push_back(x);
            top++;
        }

       /* for(int i=0; i<stackData.size(); i++)
        {
            cout <<  stackData[i] << " ";
        }
        cout << endl;*/
        
    }
    
    int pop() {
        //cout << "top : " << top << endl;
        if(top >= 0)
        {
            int value = stackData[stackData.size()-1];
            stackData.pop_back();
            top--;
            return value;
        }else{
            return -1;
        }

    }
    
    void increment(int k, int val) {
        int n=0;
        if(k<stackData.size())
        {
            n = k;
        }else{
            n = stackData.size();
        }
        for(int i=0; i<n; i++)
        {
            stackData[i] = stackData[i] + val;
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */