# 30
import sys

sys.stdin = open("10610input.txt")
T = int(input())
for test_case in range(1, T + 1):

    # str 형으로 받음
    string = input()
    arr = sorted(string, reverse=True)
    # 1. 10의 배수를 만들 수 있는가?
    result = ''
    if arr[-1] == '0':
        for s in arr:
            result += s
        if int(result) % 3 == 0:
            print(int(result))

        else:
            print(-1)
    else:
        print(-1)