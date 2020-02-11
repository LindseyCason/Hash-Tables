# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity #number of "items in the array" basically, [None, None, None, None] for a cap of 4


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        print("_hash")
        print(hash(key) % 8) #this could be a different number


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''

        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        #This is using the custom method to run this function, if there is a security breach, this will help so you can change only the custom method and it will change the rest dynamically. Use _hash_mod rather than built in hash(key)
        # index = hash(key) & self.capacity #these two are the same
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            print(f"WARNING: COLLISION AT {index}")
        else:
            self.storage[index]=(key, value) #use Tuple to store both key and value
            return




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                self.storage[index] == None
            else:
                print(f"WARNING COLLISION AT {index}")
        else:
            print(f"WARNING KEY {key} NOT FOUND")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                return self.storage[index][1] #1 IS THE VALUE 0 IS THE KEY
            else:
                print(f"WARNING COLLISION AT {index}")
                return None
        else:
            print(f"WARNING KEY {key} NOT FOUND")


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        old_storage = self.storage
        self.capacity *= 2 #This doubles
        self.storage = [None] * self.capacity #re-initialized

        for i in old_storage:
            self.insert(i[0], i[1]) #insert key and value in new storage. Insert will add this to self.storage which was set to [None] by this method. 

        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
