################ Question ######################################
# "A palindrome is a string that reads the same forward and backward"
# For example: radar or madam
# Our task is to design an optimal algorithm for checking whether 
# a given string is palindrome or not! 
################################################################

def check_palindrome_method(var_string):
    if var_string.casefold() == var_string[::-1].casefold():
        print("True! The string is a palindrome")
    else:
        print("False The string is not a palindrome")


if __name__ == "__main__":
    var_string = "Madam"
    check_palindrome_method(var_string)