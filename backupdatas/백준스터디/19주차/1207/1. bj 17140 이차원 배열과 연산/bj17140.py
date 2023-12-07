# 백준 17140. 이차원 배열과 연산
import sys
sys.stdin = open("bj17140input.txt")

# transposing 함수
def transpose(arr, N, M):
    new_arr = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            new_arr[i][j] = arr[j][i]
    return new_arr

# R, C change 함수
def change_arr(arr):
    max_col = 0

    # 새롭게 반환할 배열
    new_arr = []

    for i in range(len(arr)):
        lst = arr[i]
        # dictionary[k] : v == 해당 lst의 k의 개수가 v개
        dictionary = dict()
        for n in lst:
            if n == 0:
                continue
            dictionary.setdefault(str(n), 0)
            dictionary[str(n)] += 1
        # dictionary의 키 - 값 쌍을 담을 배열
        cnt_lst = []
        for k, v in dictionary.items():
            cnt_lst.append((int(k), v))
        # 개수 -> 숫자 순으로 정렬되게끔
        cnt_lst.sort(key=lambda x : (x[1], x[0]))

        # new_arr에 담을 일차원 배열
        new_lst = []
        for ele in cnt_lst:
            num, cnt = ele
            new_lst.append(num)
            new_lst.append(cnt)

        # 해당 배열의 길이가 100을 넘어갈 경우 잘라주기
        if len(new_lst) > 100:
            new_lst = new_lst[:100]
        # 이후 0을 채우기 위해 최대 길이 확인
        if max_col < len(new_lst):
            max_col = len(new_lst)

        new_arr.append(new_lst)

    # 각 배열 별로 부족한 개수 채우기
    for lst in new_arr:
        if max_col > len(lst):
            lst.extend([0] * (max_col - len(lst)))

    # pprint(new_arr)
    return new_arr

T = int(input())
for tc in range(T):
    # arr[R][C] = K가 되기 위한 연산의 최소 시간을 구하기 위해
    R, C, K = map(int, input().split())
    R -= 1
    C -= 1
    # 1 <= arr[i][j] <= 100
    arr = [list(map(int, input().split())) for _ in range(3)]

    # R 연산: arr의 모든 행에 대해서 정렬 (행의 개수 ≥ 열의 개수)
    # C 연산: arr의 모든 열에 대해서 정렬 (행의 개수 < 열의 개수)

    time = 0
    flag = False
    while time <= 100:
        N = len(arr)
        M = len(arr[0])

        if 0 <= R < N and 0 <= C < M and arr[R][C] == K:
            flag = True
            break

        # R연산
        if N >= M:
            arr = change_arr(arr)
        else:
            arr = transpose(arr, N, M)
            arr = change_arr(arr)
            arr = transpose(arr, len(arr), len(arr[0]))
        # for i in arr:
        #     print(i)
        # print()

        time += 1
        # print(time)

    if flag:
        print(time)
    else:
        print(-1)