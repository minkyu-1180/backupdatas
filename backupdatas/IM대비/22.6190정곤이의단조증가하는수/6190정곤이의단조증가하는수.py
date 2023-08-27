# IM 대비 22. 정곤이의 단조증가하는 수
import sys
sys.stdin = open("정곤이input.txt")


def increasing(arr, N):
    result = -1 # 단조 증가하는 수(없을 경우 -1)
    for i in range(N-1):
        for j in range(i+1, N):
            num = str(arr[i] * arr[j])
            for k in range(len(num)-1):
                # 앞쪽 자리 > 뒤쪽 자리 -> 단조증가 X -> 함수 종료
                if int(num[k]) > int(num[k+1]):
                    break
            # 단조 증가하는 수 -> 기존 단조증가수와 비교하여 갱신
            else:
                if result < int(num):
                    result = int(num)
    # 단조 증가하는 수가 없을 경우
    return result

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # Ai 개수(1 <= N <= 1000)
    arr = list(map(int, input().split()))

    result = increasing(arr, N)

    print(f'#{test_case} {result}')