from tkinter import Y
from unittest import result


a1 = int (input("enter the value in the first matrix:"))
a2 = int (input("enter the value in the first matrix:"))
a3 = int (input("enter the value in the first matrix:"))
b1 = int (input("enter the value in the first matrix:"))
b2 = int (input("enter the value in the first matrix:"))
b3 = int (input("enter the value in the first matrix:"))
c1 = int (input("enter the value in the first matrix:"))
c2 = int (input("enter the value in the first matrix:"))
c3 = int (input("enter the value in the first matrix:"))
A1 = int (input("enter the value in the second matrix:"))
A2 = int (input("enter the value in the second matrix:"))
A3 = int (input("enter the value in the second matrix:"))
B1 = int (input("enter the value in the second matrix:"))
B2 = int (input("enter the value in the second matrix:"))
B3 = int (input("enter the value in the second matrix:"))
C1 = int (input("enter the value in the second matrix:"))
C2 = int (input("enter the value in the second matrix:"))
C3 = int (input("enter the value in the second matrix:"))
x = [[a1,a2,a3],
     [b1,b2,b3],
     [c1,c2,c3]]

Y=  [[A1,A2,A3],
     [B1,B2,B3],
     [C1,C2,C3]]

result = [[0,0,0],
          [0,0,0], 
          [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j] + Y[i][j]

for r in result :
 print(r)