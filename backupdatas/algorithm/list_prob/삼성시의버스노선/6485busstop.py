# 6485. 삼성시의 버스 노선
import sys
sys.stdin = open("busstopinput.txt")

T = int(input())
for test_case in range(1, T+1):
    # 1 ~ 5000번 각 정류장을 지나는 노선
    result = [0] * 5001 # 0번 index는 안쓸거라서

    N = int(input())  # 노선의 수
    # 각 줄 별로 Ai, Bi가 주어짐
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            result[i] += 1

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]

    print(f'#{test_case}', end = ' ')
    for ele in bus_stop:
        print(result[ele], end = ' ')
    print()
