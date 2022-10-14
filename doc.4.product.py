# list product excluding duplicates
a=[6,1,3,5,6,3,1]
b=[]
product=1
i=0
while i<len(a):
    c=a[i]
    if c not in b:
        b.append(c)
        product=product*c
    i=i+1
print(b,"=",product)

# list product
a=[6,1,3,5,6,3,1]
pro=1
i=0
while i<len(a):
    c=a[i]
    pro=pro*c
    i=i+1
print(a,"=",pro)


str="kavitha023"
a=""
b=""
i=0
while i<len(str):
    if i%2!=0:
        b=b+str[i]
    else:
        a=a+str[i]
    i=i+1
print(a,b)

        
