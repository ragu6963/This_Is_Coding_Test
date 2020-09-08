import time
import sys


def Dfs(graph, node, visit, result):
    visit += [node]
    result.append(node)
    for index in range(len(graph[node])):
        next_node = graph[node][index]
        if next_node != 0 and index not in visit:
            Dfs(graph, index, visit, result)


def Bfs(graph, start):
    queue = [start]
    visit = [start]
    while queue:
        node = queue.pop(0)
        for next_node in range(len(graph[node])):
            value = graph[node][next_node]
            if value != 0 and next_node not in visit:
                visit += [next_node]
                queue.append(next_node)
    return visit


def Solve():
    sys.stdin = open("input.txt", "r")
    n, m, node = map(int, sys.stdin.readline().rstrip().split())
    visit = []
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x][y] = 1
        graph[y][x] = 1
    result = []
    Dfs(graph, node, visit, result)
    for r in result:
        print(r, end=" ")
    print()

    result = Bfs(graph, node)
    for r in result:
        print(r, end=" ")


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    # print(f"time : {start_time-end_time}")

