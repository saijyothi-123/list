a=[-12,14,95,3]
i=0
pos_count=0
neg_count=0
while i<len(a):
    if a[i]>=0:
        pos_count+=1
    else:
        neg_count+=1
    i=i+1
print(pos_count)
print(neg_count)



a=[-12,14,95,3]
pos_count=0
neg_count=0
for i in a:
    if i>=0:
        pos_count+=1
    else:
        neg_count+=1
print(pos_count)
print(neg_count)
    
