# a=[1,1,1,64,23,64,22,22,22]
# b=[]
# for i in a:
#     n=a.count(i)
#     if n==3:
#         if b.count(i)==0:
#             b.append(i)
# print(b)



a=[1,1,1,64,23,64,22,22,22]
b=[]
i=0
count=0
while i<len(a):
    if a.count(a[i])==3:
        if a[i] not in b:
            b.append(a[i])
    i=i+1
print(b)

# a=[1,1,1,64,23,64,22,22,22]
# b=[]
# for i in a:
#     if a.count(a[i])==3:
#         if a[i] not in b:
#             b.append(a[i])
# print(b)
