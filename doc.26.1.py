a=[4,5,5,5,3,8]
b=[]
for i in a:
    n=a.count(i)
    if n==3:
        if b.count(i)==0:
            b.append(i)
print(b)


a=[4,5,5,5,3,8]
b=[]
i=0
count=0
while i<len(a):
    n=a.count(i)
    if n==3:
        if b.count(i)==0:
            b.append(i)
    i=i+1
print(b)