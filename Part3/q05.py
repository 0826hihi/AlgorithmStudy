count=0
n,m=map(int,input().split())
data=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if data[i]==data[j]:
            continue
        else:
            print("(",i,",",j,")")
            count+=1

print(count)