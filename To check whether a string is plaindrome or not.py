my_str ='aIbohPhoBia'

my_str= my_str.casefold()

rev_str= reversed(my_str)
if list(my_str) == list(rev_str):
    print("the string is a plaindrome.")
else:
    print ("The string is not a plaindrome.")