############################# Question ######################################
# The problem is that we want to find duplicates in a 
# one-dimensional array of integers in O(N) running time where 
# the integer values are smaller than the length of the array!
# For example: if we have a list [1, 2, 3, 1, 5] then the algorithm
# can detect that there are a duplicate with value 1.
# Note: the array can not contain items smaller than 0 and items 
# with values greater than the size of the list. This is how we can 
# achieve O(N) linear running time complexity!
##############################################################################



def brute_force_approach(var_list):
    i = 0
    duplicate = []
    while i < len(var_list):
        j = i+1
        while j < len(var_list):
            if var_list[i] == var_list[j]:
                duplicate.append(var_list[i])
            j = j + 1
        i = i + 1
    print(set(duplicate))


def hash_maps_approach(var_list):
    duplicate = {}
    for element in var_list:
        try:
            duplicate[element] = duplicate[element] + 1
        except:
            duplicate[element] = 1
    for element in duplicate:
        if duplicate[element] > 1:
            print(element, end = " ")


def absolute_value_approach(var_list):
    for element in var_list:
        if var_list[abs(element)] >= 0:
            var_list[abs(element)] = -var_list[abs(element)]
        else:
            print("Duplicate element found ", abs(element))



if __name__ == "__main__":
    var_list = [1, 2, 1, 2, 4]
    #brute_force_approach(var_list)
    hash_maps_approach(var_list)
    #absolute_value_approach(var_list)