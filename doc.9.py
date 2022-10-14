a=[3,6,2,7,4,9]
max=a[0]
sec_max=a[0]
third_max=a[0]
i=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
i=0
while i<len(a):
    if a[i]>sec_max and a[i]!=max:
        sec_max=a[i]
        i=i+1
i=0
while i<len[a]:
    if a[i]>third_max and a[i]!=max and a[i]!=sec_max:
        third_max=a[i]
    i=i+1
print(max)
print(sec_max)
print(third_max)