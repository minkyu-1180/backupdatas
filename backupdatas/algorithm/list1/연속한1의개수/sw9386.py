# sw academy 9386. 연속한 1의 개수
import sys
sys.stdin = open("seqoneinput.txt")
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    counts = [1] * (N-1) + [arr[N-1]]

    for i in range(0, N-1):
        if arr[i] == 0:
            counts[i] = 0

        if arr[i] == arr[i+1]:
            if arr[i] == 1:
                counts[i+1] += counts[i]


    max = 0
    for i in range(N):
        if max < counts[i]:
            max = counts[i]
    print(f'#{test_case} {max}')
