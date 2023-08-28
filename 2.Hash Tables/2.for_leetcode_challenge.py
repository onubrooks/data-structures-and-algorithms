class MyHashMap(object):

    def __init__(self):
        self.BUCKET_SIZE = 1000
        self.data = [[] for _ in range(self.BUCKET_SIZE)]

    def get_index(self, bucket, key):
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return i
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        address = self._hash(key)
        bucket = self.data[address]
        index = self.get_index(bucket, key)
        if index != -1:
            bucket[index][1] = value
        else:
            bucket.append([key, value])
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        address = self._hash(key)
        bucket = self.data[address]
        index = self.get_index(bucket, key)
        if index == -1: 
            return -1
        return bucket[index][1]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        address = self._hash(key)
        bucket = self.data[address]
        index = self.get_index(bucket, key)
        if index == -1: 
            return
        del bucket[index]
    
    def _hash(self, key):
        return key % self.BUCKET_SIZE