def dfs(graph,x,y,group):
    global total
    if (x,y) in group:
        return
    group.append((x,y))
    total+=graph[x][y]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<=-1 or nx>=n or ny<=-1 or ny>=n:
            continue
        diff=max(graph[x][y],graph[nx][ny])-min(graph[x][y],graph[nx][ny])
        if l<=diff<=r:
            dfs(graph,nx,ny,group)

n,l,r=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

count=0
while True:
    result = []
    group_list=[]
    for i in range(n):
        for j in range(n):
            if (i, j) not in result:
                group = []
                total = 0
                dfs(graph, i, j, group)
                if len(group)>1:
                    group_list.append((total,group))
                    result=result+group
    if len(result)==0:
        print(count)
        break
    else:
        for g in group_list:
            for k in g[1]:
                graph[k[0]][k[1]] = g[0] // len(g[1])
        count+=1