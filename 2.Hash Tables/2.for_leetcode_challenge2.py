class MyHashSet(object):

    def __init__(self, bucket_size=1000):
        self.data = [[] for i in range(bucket_size)]
        self.bucket_size = bucket_size
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        address = self._hash(key)
        if not self.contains(key):
            self.data[address].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        address = self._hash(key)
        if self.contains(key):
            self.data[address].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        address = self._hash(key)
        return key in self.data[address]
        
    def _hash(self, key):
        return key%self.bucket_size
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)