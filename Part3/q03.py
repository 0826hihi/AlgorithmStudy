import sys
input=sys.stdin.readline().rstrip

s=list(map(int,input()))
count=[0,0]

for i in range(len(s)-1):
  if s[i]!=s[i+1]:
    count[s[i]]+=1
    if i==len(s)-2:
      count[s[i+1]]+=1

print(min(count))