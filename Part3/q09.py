import sys
input=sys.stdin.readline().strip

def solution(s):
    answer=len(s)
    # 슬라이싱은 인덱스 1개부터 최대 len(s)//2개까지 가능
    for step in range(1,len(s)//2+1):
        indexing=s[0:step]
        count=1
        strcnt=len(s)
        for i in range(step,len(s)-step+1,step):
            if indexing==s[i:i+step]:
                count+=1
                strcnt=strcnt-step+len(str(count))
                if count>2:
                    strcnt-=len(str(count-1))
            else:
                count=1
                indexing=s[i:i+step]
        answer=min(answer,strcnt)
    return answer

s=input()
print(solution(s))

