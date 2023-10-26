# 백준 1788. 피보나치 수의 확장
import sys
sys.stdin = open("bj1788input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    N = int(input())
    fibonacci = [0] * (abs(N)+1)
    result = [0, 0]
    if N == 0:
        result = [0, 0]
    else:
        fibonacci[1] = 1
        if abs(N) % 2 == 0 and N < 0:
            result[0] = -1
        else:
            result[0] = 1
        N = abs(N)
        if N > 1:
            for i in range(2, N+1):
                # 메모리 초과 피하기
                fibonacci[i] = (fibonacci[i-1] + fibonacci[i-2]) % 1000000000
        result[1] = fibonacci[N]

    print(result[0])
    print(result[1])
