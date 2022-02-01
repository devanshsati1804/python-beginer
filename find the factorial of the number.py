from math import factorial


num = int(input("enter the number for which you wantthe factorial : "))
factorial = 1
if num<0:
    print("factorial doesnot exist for the nagative number")
elif num == 0:
    print("The factorial for 0 is 0 and 1 ")
else:
    for i in range (1,num+1):
        factorial = factorial*i
    print(" the factorial of ",num,"is",factorial)
    