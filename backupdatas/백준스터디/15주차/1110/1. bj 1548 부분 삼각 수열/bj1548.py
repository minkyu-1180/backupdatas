# 백준 1548. 부분 삼각 수열
import sys
sys.stdin = open("bj1548input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # 주어지는 수의 개수(1 <= N <= 50)
    N = int(input())
    # 수열(1 <= arr[i] <= 10**9)
    arr = list(map(int, input().split()))
    # 무조건 제일 긴 길이
    if N <= 2:
        print(N)
    else:
        # 정렬하여 사용
        arr.sort()
        # 삼각 수열 : 수열의 모든 원소들에 대하여
        # 세 다른 인덱스를 골랐을 때 나온 값(A[i], A[j], A[k])에 대해
        # A[i] < A[j] + A[k], A[j] < A[i] + A[k], A[k] < A[i] + A[j]일 경우

        # i < i+k < j라 했을 때,
        # arr[i]+arr[i+k] > arr[j]인 경우, 나머지도 알아서 됨(삼각 수열 만족)
        # k = 1로 둘 경우,
        # arr[i] + arr[i+1] > arr[j] -> for k in range(1, j-i): arr[i] + arr[i+k] > arr[j]

        # 따라서, 각 i, j에 대해서 arr[i], arr[i+1], arr[j]만 비교하면 해결
        result = 2
        for i in range(N-2):
            j = i+2
            while j < N:
                # 처음으로 만족 안 할 경우, break
                if arr[i] + arr[i+1] <= arr[j]:
                    break

                # 현재의 j값에 대해 만족했을 경우, result 갱신 후 j 늘리기
                if result < j-i+1:
                    result = j-i+1
                j += 1

        print(result)