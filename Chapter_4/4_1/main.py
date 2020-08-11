import time
import sys


def Solve():
    sys.stdin = open("input.txt", "r")
    n = int(input())
    input_list = list(input().split())
    x = 1
    y = 1
    for i in input_list:
        if i == "L" and (x - 1 != 0):
            x -= 1
        if i == "R" and (x + 1 != n + 1):
            x += 1
        if i == "U" and (y - 1 != 0):
            y -= 1
        if i == "D" and (y + 1 != n + 1):
            y += 1
    print(y, x)


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

