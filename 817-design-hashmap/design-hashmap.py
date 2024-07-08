class MyHashMap(object):

    def __init__(self):
        self.myMap = {}

    def put(self, key, value):
        self.myMap[key]=value
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        

    def get(self, key):
        if key not in self.myMap:
            return -1
        for k, value in self.myMap.items():
            if k == key:
                return value
        """
        :type key: int
        :rtype: int
        """
        

    def remove(self, key):
        if key in self.myMap:
            del self.myMap[key]
        """
        :type key: int
        :rtype: None
        """
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)