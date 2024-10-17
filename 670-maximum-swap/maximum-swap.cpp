class Solution {
public:
    int maximumSwap(int num) {
        vector<int> arr;
        int n=num,q=0;
        while(n>0){
            q = n%10;
            arr.insert(arr.begin(), q);
            n = n/10;
        }
        if(arr.size()<2){
            return num;
        }
        int ind = 0;
        while(((ind+1) < (arr.size())) && arr[ind]>=arr[ind+1]){
            ind++;
        }
        int max_ind = ind;
        for(int i=ind+1; i<arr.size(); i++)
        {
            
            if(arr[i]>=arr[max_ind]){
                max_ind = i;
            }
        }
       /* if(max_ind !=0 && arr[0] < arr[max_ind]){
            int temp = arr[0];
            arr[0] = arr[max_ind];
            arr[max_ind] = temp;
        }
        else if(arr[ind]<arr[max_ind] && ind!= max_ind){
            int temp = arr[ind];
            arr[ind] = arr[max_ind];
            arr[max_ind] = temp;
          
        }*/
       // cout << "Max index : " << max_ind << endl;
        for(int i=0; i<arr.size(); i++)
        {
            if(i>=max_ind) {
                break;
            }

            if(arr[i]<arr[max_ind] && i!= max_ind){
                int temp = arr[i];
                arr[i] = arr[max_ind];
                arr[max_ind] = temp;
                break;
            }
            
        }

        
        int res =0;
        for(int i=0; i<arr.size(); i++)
        {
            res = res *10 + arr[i];
        }
        //cout << "Result : " << res << endl;
        return res;
    }
};