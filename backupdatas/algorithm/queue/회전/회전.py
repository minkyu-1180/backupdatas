# sw academy 회전
import sys
sys.stdin = open("회전input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 현재 배열의 맨 앞에 있는 원소의 idx
    front = 0
    for i in range(M):
        front = (front + 1) % N

    first = arr[front]
    print(f'#{test_case} {first}')