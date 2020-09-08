import time
import sys


def dfs(graph, index, visited):
    visited[index] = True
    print(index, end=" ")
    for i in graph[index]:
        if not visited[i]:
            dfs(graph, i, visited)


def Solve():
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7],
    ]
    visited = [False] * 9
    dfs(graph, 1, visited)


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

