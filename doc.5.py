
# while loop:

l=[1,2,2,5,8,4,4,8]
a=[]
i=0
count=0
while i<len(l):
    b=l[i]
    if b not in a:
        a.append(b)
    count=count+1
    i=i+1
print(a,"=",count)


# for loop:
l=[1,2,2,5,8,4,4,8]
a=[]
count=0
for i in range(0,len(l)):
    if l[i] not in a:
        count=count+1
        a.append(l[i])
print(a,"=",count)