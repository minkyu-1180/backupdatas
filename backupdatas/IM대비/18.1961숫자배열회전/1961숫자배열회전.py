# IM 대비 18. 숫자 배열 회전
import sys
sys.stdin = open("숫자배열회전input.txt")

def quad(arr):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][N-1-i] = arr[i][j]
    return result
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    quad1 = quad(arr)
    quad2 = quad(quad1)
    quad3 = quad(quad2)

    result1 = result2 = result3 = str()
    for i in range(N):
        for j in range(N):
            result1 += str(quad1[i][j])
            result2 += str(quad2[i][j])
            result3 += str(quad3[i][j])

    print(f'#{test_case}')
    for i in range(N):
        print(result1[i * N : (i+1) * N], result2[i * N : (i+1) * N], result3[i * N : (i+1) * N])

