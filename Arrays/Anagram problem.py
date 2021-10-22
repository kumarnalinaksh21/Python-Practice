################ Question ######################################
# Construct an algorithm to check whether two words (or phrases) 
# are anagrams or not!
# "An anagram is a word or phrase formed by rearranging the letters
# of a different word or phrase, typically using all the original 
# letters exactly once"
# For example: restful and fluster
################################################################

def check_anagram(var_string1, var_string2):
    var_list_1 = list(var_string1.casefold())
    var_list_2 = list(var_string2.casefold())
    if var_list_1.sort() == var_list_2.sort():
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    var_string_1 = "Restful"
    var_string_2 = "fluster"
    check_anagram(var_string_1, var_string_2)