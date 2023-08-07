# 17608. 막대기
import sys
sys.stdin = open("17608input.txt")
T = int(input())
for test_case in range(1, T+1):
    # 막대기 개수
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = int(input())

    # 결과를 담을 변수
    result = 0
    max_val = 0
    for i in range(N-1, -1, -1):
        if max_val < arr[i]:
            max_val = arr[i]
            result += 1
    print(result)


