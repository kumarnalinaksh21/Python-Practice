################ Question ######################################
# The problem is that we want to find duplicates in a 
# one-dimensional array of integers in O(N) running time where 
# the integer values are smaller than the length of the array!
# For example: if we have a list [1, 2, 3, 1, 5] then the algorithm
# can detect that there are a duplicate with value 1.
# Note: the array can not contain items smaller than 0 and items 
# with values greater than the size of the list. This is how we can 
# achieve O(N) linear running time complexity!
################################################################

import list

def check_duplicate_entries(var_list):
    duplicate_list = []
    temp_list = var_list
    for i in temp_list:
        if i < 0 or i > len(temp_list):
            print("the array can not contain items smaller than 0 and items with values greater than the size of the list.")
        else:
            while i < len(temp_list) - 1:
                if temp_list.sort()[i] == temp_list.sort()[i + 1]:
                    duplicate_list.append(temp_list[i])
                i = i+1
   
    if len(duplicate_list) > 0:
        print(duplicate_list, "are the duplicates in ", temp_list)
    else:
        print("no duplicates found in ", temp_list)


if __name__ == "__main__":
    var_list = [1, 2, 3, 1, 5]
    check_duplicate_entries(var_list)