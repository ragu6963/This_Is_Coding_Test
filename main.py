import time
import sys


def Solve():
    sys.stdin = open("input.txt", "r")
    input_list = map(int, input().split())


if __name__ == "__main__":
    start_time = time.time()
    Solve()
    end_time = time.time()
    print(f"time : {start_time-end_time}")

