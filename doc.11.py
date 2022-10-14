n=int(input("enter the num"))
i=0
while i<=n:
    r=n%10
    k=r**2
    n=n//10
    i=i+1
    print(k,end="")
    
    
