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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1==NULL && list2==NULL)
        {
            return list1;
        }else if(list1==NULL && list2!=NULL)
        {
            return list2;
        }else if(list2== NULL&& list1!=NULL)
        {
            return list1;
        }else if(list1->next==NULL&&list2->next==NULL)
        {
            if(list1->val<list2->val)
            {
                list1->next=list2;
                return list1;
            }else{
                list2->next=list1;
                return list2;
            }
        }
        ListNode* start_list2 = list2;
        ListNode* start_list1 = list1;
        while(start_list2!=NULL)
        {
            ListNode* new_node = new ListNode(start_list2->val);
            if(start_list1->val<new_node->val)
            {
                while(start_list1->val<new_node->val)
                {
                    if(start_list1->next!=NULL)
                    {
                        if(start_list1->next->val<new_node->val)
                        {
                            start_list1=start_list1->next;
                        }else{
                            break;
                        }
                    }else{
                        break;
                    }
                }
                new_node->next=start_list1->next;
                start_list1->next=new_node;
            }else{
                new_node->next=list1;
                list1 = new_node;
                start_list1=list1;
            }
            start_list2=start_list2->next;
        }
        return list1;
    }
};