# #%%
# class HashTable:
#     def __init__(self):
#         self.length = 100
#         self.arr = [None for i in range(self.length)]

#     def get_hash_value(self, key):
#         ascii_sum = 0

#         for char in key:
#             ascii_sum += ord(char)
#             return ascii_sum%self.length
        
#     def add_item(self, key, val):
#         hashed_val = self.get_hash_value(key)
#         self.arr[hashed_val] = val

#     def get_arr(self):
#         return self.arr


#     def get_item_at(self, key):
#         hashed_val = self.get_hash_value(key)
#         return self.arr[hashed_val]
    
#     def remove_item_at(self, key):
#         hashed_val = self.get_hash_value(key)
#         self.arr[hashed_val] = None
         

# # %%

# hash_table = HashTable()
# hash_table.add_item('veena', 20)
# hash_table.add_item('sathya', 11)
# hash_table.add_item('abc', 100)

# hash_table.get_arr()

# # %%
# print(hash_table.get_item_at('veena'))


# # %%
# hash_table.remove_item_at('abc') 
# hash_table.get_arr()

#%%

### Redo the Hash Table class to include for collision cases ###

class HashTable:
    def __init__(self):
        self.length = 100
        self.arr = [[] for i in range(self.length)]

    def get_hash_value(self, key):
        ascii_sum = 0

        for char in key:
            ascii_sum += ord(char)
            return ascii_sum%self.length
        
    def add_item(self, key, val):
        hashed_val = self.get_hash_value(key)

        found = False
        for idx, element in enumerate(self.arr[hashed_val]):
            if len(element) == 2 and element[0]==key:
                self.arr[hashed_val][idx] = (key, val)
                found = True
                break
        

        if found == False:
            self.arr[hashed_val].append((key, val))

    def get_arr(self):
        return self.arr


    def get_item_at(self, key):
        hashed_val = self.get_hash_value(key)
        for i in self.arr[hashed_val]:
            if i[0] == key:
                return i[1]


    
    def remove_item_at(self, key):
        hashed_val = self.get_hash_value(key)
        for idx, element in enumerate(self.arr[hashed_val]):
            if element[0] == key:
                del self.arr[hashed_val][idx]




#%%
hash_table = HashTable()
hash_table.add_item('veena', 20)
hash_table.add_item('sathya', 11)
hash_table.add_item('abc', 100)
hash_table.add_item('veena', 1996)

# Collision examlpe keys #
hash_table.add_item('march 6', 6)
hash_table.add_item('march 17', 17)


hash_table.get_arr()

# %%
hash_table.get_item_at("march 17")

# %%
hash_table.remove_item_at("march 17")
hash_table.get_arr()

# %%
