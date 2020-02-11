class DynamicArray:
    def __init__(self, capacity=0):
        self.count =0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    
    def insert(self, index, value): #this is a function
        if self.count == self.capacity:
            #TODO: increase size
            print("ERROR: Array is full")
            return

        if index >= self.count:
            #TODO: better error handling
            print("Index is out of bounds")
            return

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

            self.storage[index] =value
            self.count +=1
        

    def append(self, value): #this is a function
        if self.count == self.capacity:
            #TODO: increase size
            print("ERROR: Array is full")
            return 
            self.storage[self.count] =value #THE STORAGE SPACE AT THE INDEX OF THE COUNT NUMBER WILL BE ASSIGNED TO THE VALUE PASSED IN
            self.count +=1 #INCREASE THE COUNT BY 1

    def double(self):
        self.capacity *= 2
        print(self.capacity)
        new_storage = [None] * self.capacity
        print(new_storage)

        for i in range(self.count):
            new_storage[i] = self.storage[i]

            self.storage = new_storage
        print(self.storage, new_storage)



