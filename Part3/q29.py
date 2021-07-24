#손도못댄 문제

n,c=map(int,input().split())
array=[]
for _ in range(n):
    array.append(int(input()))

array.sort()
start=array[1]-array[0]
end=array[n-1]-array[0]
result = 0
while start<=end:
    mid=(start+end)//2
    count=1
    value=array[0]
    for i in range(1,n):
        if array[i]>=value+mid:
            count+=1
            value=array[i]
    if count>=c:
        result=mid
        start=mid+1
    else:
        end=mid-1

print(count)