a=[4,6,4,3,3,4,3,4,6,6]
b=[]
for i in a:
    n=a.count(i)
    if n>2:
        if b.count(i)==0:
            b.append(i)
print(b)




a=[4,6,4,3,3,4,3,4,6,6]
b=[]
i=0
count=0
while i<len(a):
    n=a.count(i)
    if n>2:
        if b.count(i)==0:
            b.append(i)
    i=i+1
print(b)