# sw academy - 4828. min max
import sys
sys.stdin = open("minmaxinput.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    # 각 양수 : 1 <= < 1000000
    arr = list(map(int, input().split()))
    min = arr[0]
    max = 1

    for i in range(N):
        if min > arr[i]:
            min = arr[i]
        if max < arr[i]:
            max = arr[i]
    result = max - min
    print(f'#{test_case} {result}')
