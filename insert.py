from multiprocessing.sharedctypes import Value
from re import I
from turtle import position


list=[10,20,30,40,50]

position=2
val=100


for i in range(len(list)-1):
    
    if i==position:
        list[i]=val
    


print(list)
      

# print(list)
           