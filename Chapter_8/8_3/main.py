import time
import sys


def Solve():
    sys.stdin = open("input.txt", "r")
    n = int(input())
    food = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = food[0]
    dp[1] = max(dp[0], food[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], food[i] + dp[i - 2])

    print(dp[n - 1])


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

