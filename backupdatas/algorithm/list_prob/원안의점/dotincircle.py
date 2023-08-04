# 16910. 원 안의 점
import sys
sys.stdin = open("dotincircleinput.txt")

T = int(input())
for test_case in range(1, T+1):
    # 반지름
    N = int(input())
    # 중심이 (0, 0)이고 반지름이 N인 원 안의 격자점 개수
    result = 0

    for x in range(-N, N+1):
        for y in range(-N, N+1):
            if x ** 2 + y ** 2 <= N**2:
                result += 1
    print(f'#{test_case} {result}')
