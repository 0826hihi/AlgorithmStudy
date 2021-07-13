import sys
input=sys.stdin.readline

n,x=map(int,input().split())
array=list(map(int,input().split()))

count=[]

def binary_search(start,end,target,count):
  if start>end:
    return
  mid=(start+end)//2
  if array[mid]==target:
    count.append(mid)
    binary_search(start,mid-1,target,count)
    binary_search(mid+1,end,target,count)
  elif array[mid]>target:
    binary_search(start,mid-1,target,count)
  else:
    binary_search(mid+1,end,target,count)
  return


binary_search(0,n-1,x,count)

if len(count)==0:
  print(-1)
else:
  print(len(count))