/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int len=0;
        ListNode* start=head;
        while(start!=NULL)
        {
            len++;
            start=start->next;
        }
        if(len==1 && n==1)
        {
            head=NULL;
            return head;
        }else if(len==2)
        {
            if(n==1)
            {
                head->next=NULL;
                return head;
            }else{
                ListNode* temp=head->next;
                return temp;
            }
        }else if(len==n)
        {
            head=head->next;
            return head;
        }
        n=len-n;
        start=head;
        for(int i=1; i<=len; i++)
        {
            if(i==n)
            {
                ListNode* temp=start->next->next;
                start->next=temp;
                return head;
            }
            start=start->next;
        }
        return head;
    }
};