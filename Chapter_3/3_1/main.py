import time
import sys


def Solve():
    sys.stdin = open("input.txt", "r")
    n = int(input())
    coin_list = [500, 100, 50, 10]
    count = 0
    while True:
        if n == 0:
            break
        for coin in coin_list:
            if n >= coin:
                print(f"거스름돈 : {coin}")
                n -= coin
                count += 1
                break
    print(count)


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

