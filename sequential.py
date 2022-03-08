n1=5
n2=10

def add_numbers(n1,n2): #function definition for addition
    sum_of_numbers = n1 + n2
    return sum_of_numbers

def subtract_numbers(n1,n2):  #function definifion for subtraction
    sub=n1-n2
    return sub

def product_num(n1, n2):  #user-defind function
    num = (n1 * n2)   #calculate product
    return num   #return value

def divide(n1, n2):
    quotient = n1 // n2
    remainder = n1 % n2
    return (quotient, remainder)    

for afunc in (add_numbers, subtract_numbers, product_num, divide):
    afunc(n1,n2)