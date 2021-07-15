from collections import deque
import copy
n,k=map(int,input().split())
graph=[[]]

# 그래프 정보 입력받기
for _ in range(n):
    graph.append([0]+list(map(int,input().split())))

s,x,y=map(int,input().split())

# 큐에 시작노드;[바이러스값,(x좌표,y좌표)] 삽입
start=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]!=0:
            start.append([graph[i][j],(i,j)])


# 입력과 동시에 시작 노드에 추가 가능.
"""            
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j]!=0:
            start.append([graph[i][j],(i,j)])
"""

# 시작 노드 바이러스 값 기준으로 오름차순 정렬
start.sort(key=lambda x:x[0])

def bfs(graph,start,s):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=deque()
    next_queue=deque()

    for i in start:
        queue.append(i[1])
    for _ in range(s):
        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=x+dy[i]
                if nx<1 or nx>n or ny<0 or ny>n:
                    continue
                if graph[nx][ny]==0:
                    next_queue.append((nx,ny))
                    graph[nx][ny]=graph[x][y]
            # 큐가 비면 증식 종료
            if len(next_queue)==0:
                return
        queue=copy.deepcopy(next_queue)
        next_queue.clear()

bfs(graph,start,s)
print(graph[x][y])