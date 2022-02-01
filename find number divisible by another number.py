from unittest import result


my_list = [12 ,23,45 ,76,86,665,7835]

result = list ( filter(lambda x : (x% 5 ==0),my_list))

print (" Number divisible by 5 are ",result)