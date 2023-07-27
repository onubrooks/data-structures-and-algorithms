"""
This is a very simple and basic implementation of a hash table.
"""
class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(self.size)]

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])) % len(self.data)
        return hash
    
    def set(self, key, value):
        address = self._hash(key)
        self.data[address].append([key, value])

    def get(self, key):
        address = self._hash(key)
        for item in self.data[address]:
            if item[0] == key:
                return item[1]
        return None
    
    def keys(self):
        keys = []
        for buckets in self.data:
            if buckets:
                for item in buckets:
                    keys.append(item[0])
        return keys
    
    def values(self):
        values = []
        for buckets in self.data:
            if buckets:
                for item in buckets:
                    values.append(item[1])
        return values

myHashTable = HashTable(50)
myHashTable.set('grapes', 10000)
print(myHashTable.get('grapes'))
myHashTable.set('apples', 9)
print(myHashTable.get('apples'))
print(myHashTable.keys())
print(myHashTable.values())