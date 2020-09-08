# 간단한 다익스트라 알고리즘
import sys

sys.stdin = open("./input.txt", "r")

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수0125
n, m = map(int, input().split())

# 시작 노드
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 리스트
graph = [[] for i in range(n + 1)]
# 방문 체크
visit = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선정보 입력
for _ in range(m):
    # a -> b 가는 비용이 c
    a, b, c, = map(int, input().split())
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    # 가장 최단 거리가 짧은 노드
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visit[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작노드에 대해 초기화
    distance[start] = 0
    visit[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visit[now] = True

        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("무한")
    else:
        print(distance[i])

