from itertools import combinations


# array로 들어온 모든 케이스 중 도시의 치킨거리 최소값을 반환하는 함수
def chick_distance(com):
    min_count = 1e9
    for case in com:
        count = 0
        for house in houses:
            # 각 집에 대한 치킨거리 계산해서 도시의 치킨거리 계산
            count += min(list(map(lambda x: abs(x[0] - house[0]) + abs(x[1] - house[1]), case)))
        min_count = min(min_count, count)
    return min_count


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

# 집, 치킨집의 좌표를 담는 리스트
stores = []
houses = []

# 집, 치킨집의 좌표를 각 리스트에 담기
for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(n):
        if graph[i][j] == 0:
            continue
        elif graph[i][j] == 1:
            houses.append((i, j))
        else:
            stores.append((i, j))

min_distance = 1e9
# 치킨집 조합 리스트 생성 후 각 조합당 도시의 치킨거리 계산
for k in range(1, m + 1):
    com = list(combinations(stores, k))  # 조합리스트 생성
    distance = chick_distance(com)
    min_distance = min(distance, min_distance)

print(min_distance)