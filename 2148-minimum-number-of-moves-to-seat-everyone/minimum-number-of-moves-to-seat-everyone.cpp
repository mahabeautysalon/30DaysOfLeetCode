class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        sort(seats.begin(),seats.end());
        sort(students.begin(),students.end());
        int i=0,j=0,moves=0;
        while(i<seats.size())
        {
            if(students[j]!=seats[i])
            {
                moves+=abs(seats[i]-students[j]);
            }
            i++;j++;
        }
        return moves;
    }
};