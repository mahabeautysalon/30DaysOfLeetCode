class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        list = set(arr)
        unique = set()
        #print(list)
        #hash_list = {}
        for val in list:
            #hash_list[val] = arr.count(val)
            if(arr.count(val) in unique):
                return False
            else:
                unique.add(arr.count(val))
            # print(unique)
        return True
            

        