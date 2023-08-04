# sw academy - 16217. 구간합
import sys
sys.stdin = open("구간합input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    # min값과 max값 정의

    # min : 최대 값인 모든 정수의 합보다는 무조건 작음
    min = 0
    for i in range(N):
        min += arr[i]
    # max : 최소 값인 9보다는 무조건 큼
    max = 9


    for i in range(N-M+1):
        # min, max와 비교할 값을 넣을 변수 생성
        num_sum = 0
        for j in range(i, i+M):
            num_sum += arr[j]
        if num_sum < min:
            min = num_sum
        if num_sum > max:
            max = num_sum
    result = max - min
    print(f'#{t} {result}')

