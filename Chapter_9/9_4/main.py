# 미래도시
import time
import sys


def Solve():
    sys.stdin = open("./input.txt", "r")
    input = sys.stdin.readline
    INF = int(1e9)
    n, m = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    for k in range(n + 1):
        for a in range(n + 1):
            for b in range(n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    x, k = map(int, input().split())
    res = graph[1][k] + graph[k][x]
    if res >= INF:
        print(-1)
    else:
        print(res)


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

