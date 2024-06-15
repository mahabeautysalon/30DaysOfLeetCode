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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* start;
        ListNode* merge=NULL;
        //cout << lists.size() << endl;
        bool check = true;
        if(lists.size()>0)
        {
            merge = lists[0];
        }
        for(int i=1; i<lists.size(); i++)
        {
            if(lists[i]!=NULL)
            {
                start = lists[i];
            }
            while(start!=NULL)
            {
                ListNode* new_node = new ListNode(start->val);
                cout << new_node->val << " ";
                ListNode* head = merge;
                check = true;
                if(head == NULL)
                {
                    merge = new_node;
                }else{
                    if(head->val>=new_node->val)
                    {
                        new_node->next = merge;
                        merge =new_node;
                    }else{
                        while(head->next!=NULL)
                        {
                            if(head->next->val >= new_node->val)
                            {
                                new_node->next = head->next;
                                head->next = new_node;
                                check = false;
                                break;
                            }
                            head = head->next;
                        }
                        if(check)
                        {
                            head->next = new_node;
                        }
                    }
                }
                
                start = start->next;
            }
        }
        //cout << "ues " << endl;
        return merge;
    }
};