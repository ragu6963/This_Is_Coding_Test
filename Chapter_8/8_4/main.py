import time
import sys


def Solve():
    sys.stdin = open("input.txt", "r")
    n = int(input())
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796
    print(dp[n])


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

