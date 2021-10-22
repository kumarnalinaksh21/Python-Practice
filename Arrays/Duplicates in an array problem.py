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



def check_duplicate_entries(var_list):
    duplicate_list = []
    for i in var_list:
        if i < 0 or i > len(var_list):
            print("the array can not contain items smaller than 0 and items with values greater than the size of the list.")
        else:
            while i < len(var_list) - 1:
                if var_list ()[i] == var_list.sort()[i + 1]:
                    duplicate_list.append(var_list[i])
                i = i+1
   
#    if len(duplicate_list) > 0:
#        print(duplicate_list, "are the duplicates in ", var_list)
#    else:
#        print("no duplicates found in ", var_list)


if __name__ == "__main__":
    var_list = [1, 2, 3, 1, 5]
    check_duplicate_entries(var_list)