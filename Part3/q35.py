n=int(input())
d=[0]*(n+1)

d[1]=1
for i in range(2,n+1):
    count=1
    while True:
        num=d[i-1]+count
        while num%5==0:
            num/=5
        while num%3==0:
            num/=3
        while num%2==0:
            num/=2
        if num==1:
            d[i]=d[i-1]+count
            break
        else:
            count+=1

print(d[n])