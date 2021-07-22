t = int(input())
result = []
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    d= [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            graph[i].append(array[m * i + j])
            if j==0:
                d[i][j]=graph[i][j]

    for j in range(1,m):
        for i in range(n):
            if i==0:
                d[i][j]=graph[i][j]+max(d[i][j-1],d[i+1][j-1])
            elif i==n-1:
                d[i][j]=graph[i][j]+max(d[i-1][j-1],d[i][j-1])
            else:
                d[i][j]=graph[i][j]+max(d[i-1][j-1],d[i][j-1],d[i+1][j-1])


    max_val=0
    for i in range(n):
        max_val=max(max_val,d[i][m-1])
    result.append(max_val)

for i in result:
    print(i)
