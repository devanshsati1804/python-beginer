from tkinter import Y


x= [[12,7,3],
    [4,5,6],
    [7,8,9]]

y=[[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result =[[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range (len(x)):
    for j in range (len (Y[0])):
        for k in range (len (Y)):
            result [i][j] += x[i][j] * Y[k][j]

for r in result :
    print (r)