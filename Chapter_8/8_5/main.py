import time
import sys


def Solve():
    sys.stdin = open("./input.txt", "r")
    n, m = list(map(int, (input().split())))
    coins = []
    dp = [10001] * (m + 1)
    for _ in range(n):
        temp = int(input())
        coins.append(temp)

    dp[0] = 0
    for index in range(coins[0], m + 1):
        for coin in coins:
            if dp[index - coin] != 10001:
                dp[index] = min(dp[index - coin] + 1, dp[index])
    print(dp)
    if dp[m] == 10001:
        print(-1)
    else:
        print(dp[m])


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

