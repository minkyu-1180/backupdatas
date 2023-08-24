# IM 대비 2. View
import sys
sys.stdin = open("Viewinput.txt")

T = 10
for test_case in range(1, T+1):
    # 건물 개수 : 4 <= N <= 1000
    N = int(input())
    # 각 건물의 높이(0 ~ 255)
    # 0, 1, N-2, N-1번 건물은 무조건 높이가 0
    arr = list(map(int, input().split()))

    result = 0
    for i in range(2, N-2):
        for j in [i-2, i-1, i+1, i+2]:
            # 자기보다 높거나 같은 건물 존재
            if arr[i] <= arr[j]:
                break
        else:
            # i번 건물의 최대조망권 수 : 높이
            # 양옆이 모두 0인 경우 : 0 0 arr[i] 0 0
            jomang = arr[i]
            for j in [i-2, i-1, i+1, i+2]:
                if jomang > arr[i] - arr[j]:
                    jomang = arr[i] - arr[j]
            result += jomang

    print(f'#{test_case} {result}')



