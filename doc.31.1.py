# print negative numbers in a given range:
# a=-4,b=5

a=int(input("enter the start point"))
b=int(input("enter the end point"))
for i in range(a,b+1):
    if i<0:
        print(i,end=",")
   
   
                                         
a=-4
b=5
for i in range(a,b+1):
    if i>=0:
        pass
    else:
        print(i,end=",")
     
     