#%%
def bubble_sort(input_list):
    for n in range(len(input_list)-1):
        # can also run only till len(input_list) - 1 - n 
        # since the last elements are already sorted as we loop through n
         for i in range(len(input_list)-1):
            if input_list[i]>input_list[i+1]:
                temp_val = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i+1] = temp_val

    return input_list



#%%

input_list = [13,11,20,9,1,30,29,15,7]

sorted_list = bubble_sort(input_list)
print(sorted_list)
# %%
