import time
import sys


def Solve():
    sys.stdin = open("input.txt", "r")
    N, M = map(int, input().split())
    result = 0
    for n in range(N):
        row = list(map(int, input().split()))
        result = max(result, min(row))
    print(result)


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

