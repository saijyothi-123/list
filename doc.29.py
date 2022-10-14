a=[5,6,[],3,[],[],9]
i=0
b=[]
while i<len(a):
    num=a[i]
    if a[i]==num and num!=[]:
        b.append(num)
    i=i+1
print(b)



a=[5,6,[],3,[],[],9]
b=[]
i=1
while i<=10:
    if i in a:
        b.append(i)
    i=i+1
print(b)