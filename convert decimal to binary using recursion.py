def convertobinary(n):
    if n>1 :
        convertobinary(n//2)
    print(n%2,end='')

decimal =int(input("Enter the decimal number: "))
convertobinary(decimal)
print()
        
    