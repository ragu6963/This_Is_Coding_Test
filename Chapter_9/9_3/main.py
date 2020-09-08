# 플로이드 워셜 알고리즘
from dis import dis
import sys

sys.stdin = open("./input.txt", "r")

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

# 2차원 리스트(그래프) 생성
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 각 간선에 대한 비용 초기화
for _ in range(m):
    # a -> b 로 가는 비용 cost
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("무한")
        else:
            print(graph[a][b], end=" ")
    print("")

