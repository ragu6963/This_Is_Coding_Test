import time
import sys


def Solve():
    sys.stdin = open("input.txt", "r")
    N, K = map(int, input().split())
    start = N
    count = 0
    it = 0
    while N >= K:
        N = N // K
        it += 1
        count += 1

    start = start - (K ** it)
    count += start
    print(count)


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

