import sys
sys.stdin = open("1032input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    result = ''
    if len(arr) == 1:
        result = arr[0]
    else:
        for j in range(len(arr[0])):
            i = 0
            while i < len(arr)-1:
                if arr[i][j] != arr[i+1][j]:
                    result += '?'
                    break
                else:
                    i += 1
                if i == len(arr)-1:
                    result += arr[0][j]
    print(result)

