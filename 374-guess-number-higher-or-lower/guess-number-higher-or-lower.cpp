/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */
#include <bits/stdc++.h>

class Solution {
public:
    int guessNumber(int n) {
        
        int start = 1,end = n;
        int num=(rand() % (end - start + 1)) + start;
        int pick = guess(num);
        while(pick != 0 && start <= end){
            if (pick == -1){
                end = num -1;
            }else if(pick == 1){
                start = num +1;
            }
            num = (rand() % (end - start + 1)) + start;
            pick = guess(num);
        }
        if (pick == 0){
            return num;
        }
        return num;
    }
};