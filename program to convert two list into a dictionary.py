# using zip and dict methords

index =[1,2,3]
language =['pyhton','c','cpp']

dictionary = dict(zip(index,language))
print (dictionary)

print()
#using the list comprehension function

index =[1,2,3]
language =['pyhton','c','cpp']

dictionary1 = {k:v for k,v in zip(index,language)}
print (dictionary1)