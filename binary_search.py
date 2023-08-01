#%%
import time

def runtime_calc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + "took" + str((end-start)*1000) + "milliseconds")
        return result
    
    return wrapper

#%%
@runtime_calc
def linear_search(input_list, val_to_search):
    for idx, val in enumerate(input_list):
        if val == val_to_search:
            return idx

@runtime_calc
def binary_search(input_list, val_to_search):
    left_idx = 0
    right_idx = len(input_list) - 1


    while left_idx <= right_idx:
        
        mid_idx = (left_idx + right_idx)//2
        mid_num = input_list[mid_idx]

        if  mid_num == val_to_search:
            return mid_idx
        
        if mid_num < val_to_search:
            left_idx = mid_idx + 1

        else:
            right_idx = mid_idx - 1

    return -1
    
@runtime_calc
def binary_search_recursive(input_list, val_to_search, left_idx, right_idx):

    if right_idx < left_idx:
        return -1
    
    mid_idx = (left_idx + right_idx)//2
    mid_num = input_list[mid_idx]

    if mid_num == val_to_search:
        return mid_idx
    
    if mid_num < val_to_search:
        return binary_search_recursive(input_list, val_to_search, mid_idx + 1, right_idx)


    else:
        return binary_search_recursive(input_list, val_to_search, left_idx, mid_idx - 1)





#%%

input_list = [i for i in range(100000)]
val_to_search = 13

val_idx = linear_search(input_list, val_to_search)
print(val_idx)
#%%
val_to_search = 14

val_idx = binary_search(input_list, val_to_search)
print(val_idx)


#%%
val_to_search = 11

val_idx = binary_search(input_list, val_to_search)
print(val_idx)

# %%
val_to_search = 3

val_idx = binary_search_recursive(input_list, val_to_search, 0, len(input_list)-1)
print(val_idx)

# %%
