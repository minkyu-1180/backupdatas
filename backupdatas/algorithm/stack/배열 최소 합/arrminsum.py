# sw academy 배열 최소 합
import sys
sys.stdin = open('arrminsuminput.txt')

def f(i, N):
    global min_sum
    # 부분집합 완성
    if i == N:
        # print(f'선택할 col idx 순서 : {P}')
        total = 0 # 해당 순열 결과를 적용했을 때 원소의 합(min_sum과 비교)
        for k in range(N):
            total += arr[k][P[k]]
        # 현재 저장된 최소 합보다 작은 케이스 발견시 갱신
        if min_sum > total:
            min_sum = total
        return
        # print(total)
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i] # 복구

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9 * N # 모든 값이 9일 경우가 최대 케이스
    P = [i for i in range(N)]

    # 함수 적용 후 갱신된 min값 반환
    f(0, N)
    print(f'#{test_case} {min_sum}')