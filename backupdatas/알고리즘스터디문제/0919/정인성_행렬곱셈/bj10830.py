# 백준 10830. 행렬 제곱
# 메모리 초과,,,,,,.ㅁㅇ리ㅏㅁㅇ리ㅜ피마ㅜ짓;
import sys
sys.stdin = open("bj10830input.txt")
import copy

# arr1 X arr2를 곱할 시 나타나는 matrix의 i, j번 idx값
def matrix_square(arr1, arr2, i, j):
    i_j = 0
    # 곱 매트릭스의 [i][j] value :
    # [i][0] * [0][j] + ... + [i][N-1] * [N-1][j]
    for k in range(N):
        plus = arr1[i][k] * arr2[k][j]
        i_j += plus
    return i_j % 1000

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # result[i] : 입력받은 arr를 i제곱하였을 때의 매트릭스(2제곱들만 찾아보기)
    result = [0] * (B+1)
    idx = 1
    result[1] = arr # arr의 1제곱 = arr
    # B제곱을 넘어가면 의미 X
    while idx * 2 <= B:
        idx = idx * 2
        # arr의 idx 제곱 매트릭스
        square = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                square[i][j] = matrix_square(result[idx//2], result[idx//2], i, j)
        result[idx] = square

    # 결과값 초기화(Identity Matrix)
    ans = [[0] * y + [1] + [0] * (N-y-1) for y in range(N)]
    # B를 binary로 -> 1인 자릿수 찾아서 제곱수 만들기
    B_to_binary = format(B, '#b')
    i = len(B_to_binary) - 1

    while B_to_binary[i] != 'b': # binary 형태 : '0bxxxxx'
        if B_to_binary[i] == '1':
            zegop = len(B_to_binary) - 1 - i
            num = 2 ** zegop
            arr_1 = copy.deepcopy(ans) # 원본 유지(밑에서 원본이 망가짐)
            for y in range(N):
                for x in range(N):
                    ans[y][x] = matrix_square(arr_1, result[num], y, x)

        i -= 1

    for i in range(N):
        for j in range(N):
            print(ans[i][j], end = ' ')
        print()
