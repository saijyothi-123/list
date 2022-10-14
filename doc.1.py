# i=0
# grocery_list=["flour","cheese","carrots"]
# while i<len(grocery_list):
#     print(i,":",grocery_list)
#     i=i+1
 
 
    
# numbers in ascending order 
a=[9,7,10,6,4]  
a.sort()
print(a)



# numbers in decending order
a=[9,7,10,6,4]
a.sort(reverse=True)
print(a)


# replace guava in place of girl
l=["apple","mango","girl","grapes"]
i=0
while i<len(l):
    if l[i]=="girl":
        l[i]="guava"
    i=i+1
print(l)
        
    