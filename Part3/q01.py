n=int(input())
array=list(map(int,input().split()))
group=[]
count=0

array.sort(reverse=False)

for i in array:
    group.append(i)
    if i==len(group):
        count+=1
        group=[]

print(count)