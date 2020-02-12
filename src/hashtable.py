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
        if self.storage[self._hash_mod(key)] != None: #IF THERE IS SOMETHING THERE
            current = self.storage[self._hash_mod(key)]#SET CURRENT TO THE NODE
            while current: #WHILE A NODE EXISTS
                if current.key == key: #IF THE KEY MATCHES
                    current.value = value #REASSIGN THE VALUE
                    break
                if current.next != None: #IF AT THE END OF THE LINE...
                    current = current.next #SET CURRENT TO NOW BE THE NEXT NODE AFTER CURRENT
                else:
                    break
            current.next = LinkedPair(key, value)#IF NO NODE AT NEXT, INSERT LINKED PAIR
        else:
            self.storage[self._hash_mod(key)] = LinkedPair(key, value) #IF NO NODES EXIST AT ALL, INSERT NODE AS LINKED PAIR


    def remove(self, key):
        # index = self._hash_mod(key) #get index for that key again
        if self.storage[self._hash_mod(key)] != None:#IF A NODE EXISTS
            previous=None
            current = self.storage[self._hash_mod(key)] #SET CURRENT TO THE NODE
            next = current.next
            while True: #while above is NOT NONE
                if current.key == key: #IF THE CURRENT.KEY MATCHES THE KEY
                    if previous != None and next != None: #IF THE NODE IS IN THE MIDDLE OF THE BUNCH
                        previous.next = next #Set the next node after the previous node to the NEXT node, eliminating the current node
                        break
                    if previous == None and next != None: #IF THE NODE IS AT THE HEAD AND THERE IS A NEXT NODE...
                        self.storage[self._hash_mod(key)] = next #SET THE CURRENT NODE TO THE "NEXT" NODE ELIMINATING NODE
                        break
                    if previous == None and next == None:#IF THERE IS NO PREVIOUS AND THERE IS NO NEXT, JUST A STAND ALONE NODE
                        self.storage[self._hash_mod(key)] = None#SET THAT NODE TO NONE
                        break
                    if previous != None and next == None: #IF THERE IS A PREVIOUS AND NO NEXT, IT'S AT THE TAIL END
                        previous.next = None #SET THE NEXT TO THE PREVIOUS, TO NONE
                        break
                elif current.next != None: #IF THE KEY DOESN'T MATCH, MOVE THE NODES IN THE ORDER BELOW AND RETRY
                    previous=current
                    current=current.next
                    next=current.next
            else: #IF WE'RE OUT OF THINGS TO CHECK AND NO KEY MATCHED
                print(f"WARNING KEY {key} NOT FOUND")
        else:
            print(f"WARNING KEY {key} NOT FOUND")







    def retrieve(self, key):
        if self.storage[self._hash_mod(key)] != None: #IF THE SPOT YOU'RE AT IS NOT EMPTY
            current = self.storage[self._hash_mod(key)] #SET THAT SPOT TO CURRENT
            while True: #WHILE THERE IS A CURRENT ASSIGNED (NOT NONE)
                if current.key == key: #IF THE KEY OF THE CURRENT MATCHES THE KEY PASSED IN
                    return current.value #RETURN THE VALUE THAT BELONGS TO THAT KEY
                elif current.next != None: #IF YOU'RE AT THE END OF THE STORAGE
                    current=current.next #SET THE CURRENT TO THE NEXT NODE AND KEEP TRYING
                else:
                    return None #IF ALL ELSE FAILS
        else:
            print(f"WARNING KEY {key} NOT FOUND")
            return None






    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        old_storage = self.storage #SET THE CURRENT STORAGE TO THE OLD STORAGE VARIABLE TO SAVE IT FOR LATER, WE'LL BE PUTTING THIS BACK INTO THE NEW STORAGE ONCE IT'S RESIZED
        self.capacity *= 2 #DOUBLING THE CAPICITY
        self.storage = [None] * self.capacity #REINITIALIZED THE STORAGE WITH THE NEW SIZE STORAGE.
        for item in old_storage:#FOR EVERY ITEM IN OLD_STORAGE
            if item !=None: #AS LONG AS THAT ITEM != NONE
                current = item #SET NON-NONE ITEM TO CURRENT
                while current:#WHILE A CURRENT IS ASSIGNED...
                    self.insert(current.key, current.value) #INSERT KEY AND VALUE OF OLD STORAGE TO NEW STORAGE. Insert will add this to self.storage which was set to [None] by this method. 
                    current = current.next#THEN SENT CURRENT TO THE NEXT ITEM, IF IT'S NOT NONE AND REPEAT
        print("new storage", self.storage)
        print("old storage", old_storage)

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
