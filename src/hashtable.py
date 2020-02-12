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
        self.capacity = capacity  # Number of buckets/items/spaces in the hash table
        self.storage = [None] * capacity #number of "items in the array" basically, [None, None, None, None] for a cap of 4


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key) #this(SELF.CAPACITY) needs to be the length of the array or the capacity so the index will not be outside the array indexs
        #HERE WE ARE JUST USING THIS _HASH AS A PRIVATE METHOD IN CASE SOMETHING WAS TO CHANGE ABOUT THE BUILT IN METHOD HASH LATER DOWN THE ROAD, WE COULD UPDATE THIS IN ONE SPOT AND THE CHANGES WOULD TAKE EFFECT THROUGHOUT.



    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        #TODO

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        #THIS IS THE USING THE ABOVE PRIVATE _HASH AND RETURNING THE MODULUS OFTHE HASH TO BE USED AS AN INDEX LATER

        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        #This is using the private method to run this function, if there is a security breach, this will help so you can change only the custom method and it will change the rest dynamically. Use _hash_mod rather than built in hash(key)
        # index = hash(key) & self.capacity #these two are the same
        index = self._hash_mod(key) #creates an index
        if self.storage[index] is not None: #check to see if index is empty (should be), if not, print a collision warning
            print(f"WARNING: COLLISION AT {index}")
        else:#if it is empty, it's available for use. Store the key,value pair at the index because it is available. see below
            self.storage[index]=(key, value) #use Tuple to store both key and value
            return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key) #get index for that key again
        if self.storage[index] is not None: #if it's not empty (if something is in there)
            if self.storage[index][0] == key: #the 0 element in the tuple(key,value) is the key, 1 element is value
                self.storage[index] == None #reset the info at that index to None which is removing the key,value pair
            else:
                print(f"WARNING COLLISION AT {index}")
        else:
            print(f"WARNING KEY {key} NOT FOUND")

    def retrieve(self, key): #this is the same as get
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key) #get the index of the key again
        if self.storage[index] is not None: #if it's not empty
            if self.storage[index][0] == key: #they 0 element is the key and the 1 element is the value
                return self.storage[index][1] #return the value, because we are retrieving (getting).
            else:
                return None
        else:
            print(f"WARNING KEY {key} NOT FOUND")


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        old_storage = self.storage #set old storage to the current storage that we are about to reset, this saves it in old_storage
        self.capacity *= 2 #This doubles the capicity
        self.storage = [None] * self.capacity #re-initialized the storage with now double space. THEN below, we will add our old storage back into the newly doubled storage.

        for i in old_storage:
            self.insert(i[0], i[1]) #insert key and value in new storage. Insert will add this to self.storage which was set to [None] by this method. 



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
