# 개선된 다익스트라 알고리즘
from dis import dis
import sys
import heapq

sys.stdin = open("./input.txt", "r")

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수0125
n, m = map(int, input().split())

# 시작 노드
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선정보 입력
for _ in range(m):
    # a -> b 가는 비용이 c
    a, b, c, = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작노드로 가기위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않으면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미처리된 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접노드 확인
        for i in graph[now]:
            # i[0] 은 현재 노드와 연결된 다른 노드
            # i[1] 은 현재 노드에서 다른 노드로 이동하는 비용
            # cost = 현재 노드까지의 비용 + 다른 노드로 이동하는 비용
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("무한")
    else:
        print(distance[i])

