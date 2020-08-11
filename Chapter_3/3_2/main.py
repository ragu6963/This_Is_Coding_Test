import time
import sys


def Solve():
    sys.stdin = open("input.txt", "r")
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    data = sorted(data, reverse=True)
    result = 0
    k = 0
    m = 0
    while m != M:
        result += data[0]
        m += 1
        k += 1
        if k == K:
            k = 0
            m += 1
            result += data[1]
    print(result)


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

