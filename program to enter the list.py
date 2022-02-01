listA =[]

n =int(input("Enter the number of elements in the list: "))

for i in range(0,n):
    print("Enter the element no- {0}".format(i+1) )
    elm=int(input())
    listA.append(elm)

print("the entered list is :\n",listA)

    