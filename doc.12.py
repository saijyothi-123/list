a=int(input("enter the num"))
b=[]
i=1
while i<=a:
    x=int(input("enter the num"))
    b.append(x)
    num=x
    r=num%1000
    m=r%100
    n=m%10
    i=i+1
    print(num-r,"+",r-m,"+",m-n,"+",n)
    