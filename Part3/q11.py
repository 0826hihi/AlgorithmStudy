from collections import deque
n=int(input())
graph=[[0]*(n+1) for _ in range(n+1)]
k=int(input())
for _ in range(k):
  p,q=map(int,input().split())
  graph[p][q]=1

#동,남,서,북
directions=[(0,1),(1,0),(0,-1),(-1,0)]
#처음위치
dx=[0,1,0,-1]
dy=[1,0,-1,0]
pd=0
ch=[None]*10001

#위치 입력
l=int(input())
for _ in range(l):
  time,d=input().split()
  ch[int(time)]=d

snake=deque([(1,1)])
t=0
x,y=1,1

while True:
  t+=1
  x+=dx[pd]
  y+=dy[pd]
  if x<1 or x>n or y<1 or y>n or (x,y) in snake:
    break
  if graph[x][y]==1:
    graph[x][y]=0
  else:
    snake.popleft()
  snake.append((x,y))
  if ch[t]=='D':
    pd=(pd+1)%4
  elif ch[t]=='L':
    pd=(pd-1)
    if pd==-1:
      pd+=4

print(t)