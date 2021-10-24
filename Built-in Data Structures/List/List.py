# List in Python are ordered and have a definite count. 
# The elements in a list are indexed according to a definite 
# sequence and the indexing of a list is done with 0 being the first index. 
# Each element in the list has its definite place in the list.
# This allows duplicating of elements in the list, with each element having its own distinct place and credibility.


#-------------------------------- Creating a list-----------------------------------------------------------------#
# Lists in Python can be created by just placing the sequence inside the square brackets[].

var_list = [] # this is an empty list

#-------------------------------- Adding elements to a list-------------------------------------------------------#
# append() method adds at the end of a list. Tuples or existing lists can be added to a list using this method
# insert(position, value) method adds at custom position within the list.
# extend() method adds multiple elements to the end of the list.

for i in range(1,10):
    var_list.append(i)
print(var_list, " via append method")


temp_list = [81]
var_list.append(temp_list)
print(var_list, " after appending temp list to the main list")


var_list.insert(9, 10)
print(var_list, " after insert")

var_list.extend([21, "hello Kitty", 22])
print(var_list, " after extend method")

var_list.extend(temp_list) 
print(var_list, "  extend method adds other list elements to main list")


#-------------------------------- Removing elements from the List-------------------------------------------------------#
# remove() method removes the specified item but an Error arises if element doesn’t exist in the set.
# Pop() function by default removes only the last element of the set, 
# to remove element from a specific position of the List, index of the element is passed as an argument to the pop() method.

var_list.remove([81])
print(var_list, "  after remove method")

var_list.pop()
print(var_list, "  after default pop method")

for i in range(1,5):
    var_list.pop(i)
    print(var_list, "  during custom pop method")


