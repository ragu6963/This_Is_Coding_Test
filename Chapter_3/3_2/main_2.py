import time
import sys


def Solve():
    sys.stdin = open("input.txt", "r")
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    data = sorted(data, reverse=True)
    first = data[0]
    second = data[1]
    split = first * K + second
    result = split * (M // (K + 1)) + first * (M % (K + 1))
    print(result)


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

