from ast import Num
from enum import Flag


num = int (input("Enter the number to chech weather its prime or not : "))
Flag = False
 
if num>1 :
    for i in range(2,num):
     if (num% i) == 0:
        Flag = True
        break
if Flag:
    print(num," is not a prime number")
else:
    print(num, " is a prime number")
    
    