import numpy as np


lista= np.array([[0,2,0,4,3,5,],[6,7,-9,8,-2,9]])

min=lista[0,0]
min2=lista[1,0]
for x in lista:
    print(x)
    for y in x:
        print(y)
        if y<lista[0,0]:
            min=y

print(min)