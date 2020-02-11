import hashlib

key=b"str" #the b removes all other str methods. normal str is an object. To hash a string you need the b 
my_string="this is a normal string" #which is an object

for i in range(10):
    hashed = hashlib.sha256(key).hexdigest()
    print(hashed)

for i in range(10):
    hashed = hash(key)
    print(hashed % 8)