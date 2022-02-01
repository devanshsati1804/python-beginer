from unicodedata import digit


low = int (input ("Enter the lower number "))
up = int (input ("Enter the lower number "))

for num in range (low,up+1):
    order = len(str(num))
    sum =0
    temp = num
    while temp>0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
if num == sum :
    print(num)