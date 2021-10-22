################ Question ######################################
# The problem is that we want to reverse a T[] array 
# in O(N) linear time complexity and we want the algorithm 
# to be in-place as well - so no additional memory can be used!
# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]
################################################################

def reverse(var_array):
    head = 0
    tail = len(var_array) - 1
    while tail > head:
        temp_var = var_array[head]
        var_array[head] = var_array[tail]
        var_array[tail] = temp_var
        head = head + 1
        tail = tail - 1
    print(var_array)

if __name__ == "__main__":
    var_array = [1,2,3,4,5,6,7,8,9,10]
    reverse(var_array)