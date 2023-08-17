# sw academy 암호생성기
import sys
sys.stdin = open("암호생성기input.txt")

for test_case in range(10):
    t = int(input())
    arr = list(map(int, input().split()))

    f = 0
    while arr[f] != 0:
        for c in range(1, 6):
            if arr[f] - c > 0:
                arr[f] = arr[f] - c
                f = (f + 1) % len(arr)
            else:
                arr[f] = 0
                break
    # f : 0이 된 idx
    f = (f+1) % len(arr)
    # print(arr)

    print(f'#{t}', end = ' ')
    for i in range(f, len(arr)):
        print(arr[i], end = ' ')
    for i in range(f):
        print(arr[i], end = ' ')
    print()


