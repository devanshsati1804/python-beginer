# using the splitext() method from the os module

import os
path = input("Enter the path of the file")
file_details = os.path.splitext(path)
print(file_details)
print(file_details[1])

print()
# using pathlib module

import pathlib
print(pathlib.Path(path).suffix)