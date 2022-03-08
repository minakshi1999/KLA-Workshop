import logging
from time import sleep
import time

import yaml
from yaml.loader import SafeLoader

logging.basicConfig(filename='sequential.log',level=logging.DEBUG,
                    format='%(asctime)s %(message)s')

n1=5
n2=10

def add_numbers(n1,n2): #function definition for addition
    logging.debug("This is the add_number")
    sum_of_numbers = n1 + n2
    return sum_of_numbers

def subtract_numbers(n1,n2):  #function definifion for subtraction
    logging.debug("This is the subtract_numbers")
    sub=n1-n2
    return sub

def product_num(n1, n2):  #user-defind function
    logging.debug("This is the product_num")
    num = (n1 * n2)   #calculate product
    return num   #return value

def divide(n1, n2):
    logging.debug("This is the devide")
    quotient = n1 // n2
    remainder = n1 % n2
    return (quotient, remainder)    

for afunc in (add_numbers, subtract_numbers, product_num, divide):
    afunc(n1,n2)

