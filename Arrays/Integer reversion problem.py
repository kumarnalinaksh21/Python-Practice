################ Question ######################################
# Our task is to design an efficient algorithm to reverse a given 
# integer. For example if the input of the algorithm is 1234 then
# the output should be 4321.
################################################################

def reverse_integer(num):
    reverse_number = 0
    while num > 0 :

        remainder = int (num % 10)
        reverse_number = reverse_number * 10 + remainder
        num = num // 10
    print(reverse_number)



if __name__ == "__main__":
    reverse_integer(2021)