def solution(N, stages):
    answer=[]
    count=[0]*(N+1)
    challenging=[0]*(N+1)
    for stage in stages:
        for i in range(stage):
            count[i]+=1
        challenging[stage-1]+=1

    for i in range(N):
        if count[i]==0:
            result=0
        else:
            result=challenging[i]/count[i]
        answer.append((result,i+1))

    answer.sort(key=lambda x:(-x[0],x[1]))
    for i in range(N):
        answer[i]=answer[i][1]
    return answer