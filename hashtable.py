class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, string):
        sum = 0
        for char in string:
            sum += ord(char)
        return sum
    
    def add(self, key, value):

        hash_key = self.hash(key)
        
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        
        self.collection[hash_key][key] = value

    def remove(self, key):

        hash_key = self.hash(key)
        if hash_key in self.collection:
            self.collection[hash_key].pop(key, None)
    
    def lookup(self, key):

        hash_key = self.hash(key)
        if hash_key in self.collection:
            return self.collection[hash_key].get(key)
        return None


hashtable = HashTable()
hashtable.add("hola", "mundo")
hashtable.add("aloh", "submundo")
hashtable.add("sol", "brillante")
print(hashtable.collection)
