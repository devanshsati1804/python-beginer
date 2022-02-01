def print_factors (x):
    print("The factors of ",x, " are:")
    for i in range (1,x+1):
        if x %i ==0:
            print(i)

x = int(input("enter the num "))
print(print_factors(x))

    