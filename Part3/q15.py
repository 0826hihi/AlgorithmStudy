from collections import deque
n,m,k,x=map(int,input().split())
graph=[[] for i in range(n+1)]
distance=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

def bfs(x):
    queue=deque([x])
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if distance[i]==0:
                queue.append(i)
                distance[i]=distance[now]+1


bfs(x)

array=[]

for i in range(1,n+1):
    if distance[i]==k:
        array.append(i)

if len(array)==0:
    print(-1)
else:
    array.sort()
    for i in array:
        print(i)
