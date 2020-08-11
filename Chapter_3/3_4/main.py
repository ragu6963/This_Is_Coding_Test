import time
import sys


def Solve():
    sys.stdin = open("input.txt", "r")
    N, K = map(int, input().split())
    start = 1
    count = 0
    while start != N:
        if start * K <= N:
            start *= K
            count += 1
        else:
            start += 1
            count += 1
    print(count)


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

