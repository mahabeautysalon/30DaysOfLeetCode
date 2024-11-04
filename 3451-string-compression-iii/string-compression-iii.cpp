class Solution {
public:
    string compressedString(string word) {
        int count = 1;
        string result = "";
        if(word.size() == 1){
            result += '1';
            result += word;
            return result;
        }
        for(int i=0; i<word.size(); i++){
            if(word[i] != word[i+1]){
                if (count == 0){
                    count = 1;
                }
                
                if(count < 9 && count > 0){
                    result += (count + 48);
                    result += word[i];
                    count = 1;
                }else{
                    while(count > 0){
                        if(count > 9 ){
                            result += '9';
                            result += word[i];
                            count -= 9;
                        }else if(count > 0){
                            result += (count + 48);
                            result += word[i];
                            count =0;
                        }
                        
                    }
                    count = 1;
                }
            }else{
                count++;
            }
        }
        return result;
    }
};