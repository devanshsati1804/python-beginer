a = float(input ("enter the first digit :"))
b= float(input (" enter the second digit: "))
c = float(input(" Enter the third digit: "))

if (a>=b)and (a>=c):
    largest = a
elif (b>=a)and (b>=c):
    largest= b
else:
    largest=c

print("the largest number is ", largest)
        