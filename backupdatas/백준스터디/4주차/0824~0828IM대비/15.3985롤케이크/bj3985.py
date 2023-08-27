# IM 대비 15. 백준 3985 롤케이크
import sys
sys.stdin = open("3985롤케이크input.txt")

T = int(input())
for test_case in range(1, T+1):
    L = int(input())
    N = int(input())

    arr = [0] * (L+1)
    result1 = 0
    result2 = 0
    max_c1 = 0
    max_c2 = 0
    for i in range(1, N+1):
        P, K = map(int, input().split())
        # 가장 많은 조각을 기대한 사람
        if max_c1 < K-P+1:
            max_c1 = K-P+1
            result1 = i

        c = 0
        for x in range(P, K+1):
            if arr[x] == 0:
                c += 1
                arr[x] = i
        if max_c2 < c:
            max_c2 = c
            result2 = i
    print(result1)
    print(result2)
