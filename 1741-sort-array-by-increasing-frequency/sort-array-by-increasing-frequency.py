class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = {}
        for val in nums:
            if dic.get(val):
                dic[val] +=1
            else:
                dic[val]=1
        sorted_dict = dict(sorted(dic.items(), key=lambda item: (item[1],-item[0])))
        #print(sorted_dict)
        ans = []
        for key in sorted_dict:
            temp = [key]*sorted_dict[key]
            ans.extend(temp)
        return ans