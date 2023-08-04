# 2167. 2차원 배열의 합
import sys
sys.stdin = open("2167input.txt")
input = sys.stdin.readline


# 배열의 크기
N, M = map(int, input().split())
# N X M 2차원 배열 생성
arr = [list(map(int, input().split())) for _ in range(N)]
# 합을 구할 부분의 개수
K = int(input())

# 겉을 0으로 도배
# 함수 1

sum_arr = [[0] * M for _ in range(N)]


# 누적합

sum_arr[0][0] = arr[0][0]
add = 0
for x in range(M):
    add += arr[0][x]
    sum_arr[0][x] = add
print(sum_arr)

'''
def scope_sum(sum_arr, x1, y1, x2, y2):

    result = sum_arr[y2][x2]
    if x1 > 0:
        result -= sum_arr[y2][x1-1]
    if y1 > 0:
        result -= sum_arr[y1-1][x2]
    if x1 > 0 and y1 > 0:
        result += sum_arr[y1-1][x1-1]

    return result

    if x1 > 0 and y1 > 0:
        result = sum_arr[y2][x2] - (sum_arr[y1 - 1][x2] + sum_arr[y2][x1 - 1] - sum_arr[y1 - 1][x1 - 1])
    elif x1 > 0:
        result = sum_arr[y2][x2] - sum_arr[y2][x1-1]
    elif y1 > 0:
        result = sum_arr[y2][x2] - sum_arr[y1-1][x2]
    else:
        result = sum_arr[y2][x2]
    return result


for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    y1, x1, y2, x2 = y1-1, x1-1, y2-1, x2-1
    result = scope_sum(sum_arr, x1, y1, x2, y2)
    print(result)











# 함수 2
def scope_sum(sum_arr, x1, y1, x2, y2):
    result = sum_arr[y2][x2] - (sum_arr[y1-1][x2] + sum_arr[y2][x1-1] - sum_arr[y1-1][x1-1])
    return result


sum_arr = [[0] * (M+1) for _ in range(N+1)]
for y in range(1, N+1):
    for x in range(1, M+1):
        sum_arr[y][x] = sum_ele(my_arr, y, x)


for i in range(1, N+1):
    for j in range(1, M+1):
        sum_arr[i][j] = sum_ele(my_arr, i, j)

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    result = scope_sum(sum_arr, x1, y1, x2, y2)
'''