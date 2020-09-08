import time
import sys


def Solve():
    sys.stdin = open("input.txt", "r")
    n = int(input())
    dp = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        if i % 5 == 0:
            dp[i] = min(dp[i // 5] + 1, dp[i - 1] + 1)
            pass
        elif i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
            pass
        elif i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
            pass
        else:
            dp[i] = dp[i - 1] + 1
            pass
        print(i, dp[i])

    print(dp[n])


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

