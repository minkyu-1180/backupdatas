# 백준 3967. 매직 스타
import sys
sys.stdin = open("bj3967input.txt")
from copy import deepcopy

'''
계산
1. 0 2 5 7
2. 0 3 6 10
3. 1 2 3 4
4. 1 5 8 11
5. 7 8 9 10
6. 4 6 9 11
'''
'''
     0
1  2  3  4
  5    6
7  8  9  10
    11
'''
def check(now):
    c1 = (ord(now[0]) - 64) + (ord(now[2]) - 64) + (ord(now[5]) - 64) + (ord(now[7]) - 64)
    c2 = (ord(now[0]) - 64) + (ord(now[3]) - 64) + (ord(now[6]) - 64) + (ord(now[10]) - 64)
    c3 = (ord(now[1]) - 64) + (ord(now[2]) - 64) + (ord(now[3]) - 64) + (ord(now[4]) - 64)
    c4 = (ord(now[1]) - 64) + (ord(now[5]) - 64) + (ord(now[8]) - 64) + (ord(now[11]) - 64)
    c5 = (ord(now[7]) - 64) + (ord(now[8]) - 64) + (ord(now[9]) - 64) + (ord(now[10]) - 64)
    c6 = (ord(now[4]) - 64) + (ord(now[6]) - 64) + (ord(now[9]) - 64) + (ord(now[11]) - 64)
    if c1 == c2 == c3 == c4 == c5 == c6 == 26:
        return True
    return False
bests = []
def backtracking(now, cnt, k):
    global best
    if cnt == 12:
        if check(now):
            # print(now)
            if best == []:
                best = deepcopy(now)
            else:
                for i in range(12):
                    if best[i] < now[i]:
                        return
                best = deepcopy(now)
                # print(best)
        return

    # 해봤자 이미 사전순으로 앞서는 경우가 있음
    if best:
        for i in range(len(now)):
            if best[i] < now[i]:
                return

    index = wtc[k]
    for i in range(1, 13):
        if visited[i] == 0:
            visited[i] = 1
            now[index] = chr(i+64)
            backtracking(now, cnt+1, k+1)
            visited[i] = 0
            now[index] = 'x'

arr = [list(input()) for _ in range(5)]
start_lst = []

cnt = 0
visited = [0] * 13
wtc = []
c = 0
for i in range(5):
    for j in range(9):
        if arr[i][j] == '.':
            continue

        start_lst.append(arr[i][j])
        if arr[i][j] != 'x':
            visited[ord(arr[i][j]) - 64] = 1
            cnt += 1
            # print(c)
        else:
            wtc.append(c)
        c += 1
# print(wtc)
best = []
# print(start_lst)
# print(visited)

backtracking(start_lst, cnt, 0)
# print(best)


result = [['.'] * 9 for _ in range(5)]
coordinates = [(0, 4),
               (1, 1), (1, 3), (1, 5), (1, 7),
               (2, 2), (2, 6),
               (3, 1), (3, 3), (3, 5), (3, 7),
               (4, 4)]
idx = 0
for i, j in coordinates:
    result[i][j] = best[idx]
    idx+=1

for lst in result:
    string = ''
    for s in lst:
        string += s
    print(string)







#
#
#
# arr = [list(input()) for _ in range(5)]
# # start = ['' for _ in range(12)]
#
# start = deepcopy(arr)
# coordinates = [(0, 4),
#     (1, 1), (1, 3), (1, 5), (1, 7),
#         (2, 2),         (2, 6),
#     (3, 1), (3, 3), (3, 5), (3, 7),
#                (4, 4)]
#
# idx = 0
#
# visited = [0] * 13
#
# for i in range(5):
#     for j in range(9):
#         if arr[i][j].isalpha():
#             start[idx] = arr[i][j]
#             idx += 1
#             if arr[i][j] != 'x':
#
#                 visited[ord(arr[i][j])-64] = 1
# print(start)
# # apb = [chr(i) for i in range(ord('A'), ord('L')+1)]
# # print(apb)
# '''
# 계산해야 하는 좌표
# 1. 0 2 5 7
# 2. 0 3 6 10
# 3. 1 2 3 4
# 4. 1 5 8 11
# 5. 7 8 9 10
# 6. 4 6 9 11
# '''
# def check():
#     c1 = ord(start[coordinates[0][0]][coordinates[0][1]]) + ord(start[coordinates[2][0]][coordinates[2][1]]) +
#     ord(start[coordinates[5][0]][coordinates[5][1]]) + ord(start[coordinates[7][0]][coordinates[7][1]])
#     c2 = ord(start[coordinates[0][0]][coordinates[0][1]]) + ord(start[coordinates[3][0]][coordinates[3][1]]) +
#     ord(start[coordinates[6][0]][coordinates[6][1]]) + ord(start[coordinates[10][0]][coordinates[10][1]])
#     c3 = ord(start[coordinates[1][0]][coordinates[1][1]]) + ord(start[coordinates[2][0]][coordinates[2][1]]) +
#     ord(start[coordinates[3][0]][coordinates[3][1]]) + ord(start[coordinates[4][0]][coordinates[4][1]])
#     c4 = ord(start[coordinates[1][0]][coordinates[1][1]]) + ord(start[coordinates[5][0]][coordinates[5][1]]) +
#     ord(start[coordinates[8][0]][coordinates[8][1]]) + ord(start[coordinates[11][0]][coordinates[11][1]])
#     c5 = ord(start[coordinates[7][0]][coordinates[7][1]]) + ord(start[coordinates[8][0]][coordinates[8][1]]) +
#     ord(start[coordinates[9][0]][coordinates[9][1]]) + ord(start[coordinates[10][0]][coordinates[10][1]])
#     c6 = ord(start[coordinates[4][0]][coordinates[4][1]]) + ord(start[coordinates[6][0]][coordinates[6][1]]) +
#     ord(start[coordinates[9][0]][coordinates[9][1]]) + ord(start[coordinates[11][0]][coordinates[11][1]])
#
#     if not (ord(start[0]) + ord(start[2]) + ord(start[5]) + ord(start[7]) == 22 + ord('A')*4):
#         return False
#     if not (ord(start[1]) + ord(start[2]) + ord(start[3]) + ord(start[4]) == 22 + ord('A')*4):
#         return False
#     if not (ord(start[0]) + ord(start[3]) + ord(start[6]) + ord(start[10]) == 22 + ord('A')*4):
#         return False
#     if not (ord(start[7]) + ord(start[8]) + ord(start[9]) + ord(start[10]) == 22 + ord('A')*4):
#         return False
#     if not (ord(start[1]) + ord(start[5]) + ord(start[8]) + ord(start[11]) == 22 + ord('A')*4):
#         return False
#     if not (ord(start[4]) + ord(start[6]) + ord(start[9]) + ord(start[11]) == 22 + ord('A')*4):
#         return False
#     return True
# ans = []
# flag = False
# def magic_star(cur, mstar,):
#     global ans, flag
#     if flag:
#         return
#     if cur == 12:
#         if check():
#             flag = True
#             ans = mstar[:]
#         return
#     if mstar[cur] != 'x':
#         magic_star(cur+1, mstar)
#     else:
#         for i in range(1, 13):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 mstar[cur] = chr(i+64)
#                 magic_star(cur+1, mstar)
#                 visited[i] = 0
#                 mstar[cur] = 'x'
#                 if flag:
#                     return
#         # for i in range(len(apb)):
#         #     if not visited[apb[i]]:
#         #         mstar[cur] = apb[i]
#         #         visited[apb[i]] = True
#         #         magic_star(cur+1, mstar)
#         #         visited[apb[i]] = False
#         #         mstar[cur] = 'x'
#         #         if flag:
#         #             return
# magic_star(0, start)
# idx = 0
# for i in range(5):
#     for j in range(9):
#         if arr[i][j].isalpha():
#             arr[i][j] = ans[idx]
#             idx += 1
# for i in range(5):
#     print(''.join(arr[i]))
