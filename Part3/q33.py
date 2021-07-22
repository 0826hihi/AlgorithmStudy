n=int(input())
array=[]
for _ in range(n):
    t,p=map(int,input().split())
    array.append((t,p))
d=[0]*(n+1)
for i in range(n):
    if i+array[i][0]>n:
        continue
    max_val=max(d[i+array[i][0]],d[i]+array[i][1])
    for j in range(i+array[i][0],n+1):
        d[j]=max(d[j],max_val)
print(max(d))