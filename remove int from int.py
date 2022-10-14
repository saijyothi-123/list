
    
str="jyothi223harijana"
i=0
b=[]
p=""
while i<len(str):
    if str[i].isdigit():
        b.append(str[i])
    i+=1
p="".join(b)
print(p)



i=0
b=[]
p=""
while i<len(str):
    if str[i].isalpha():
        b.append(str[i])
    i+=1
p="".join(b)
print(p)