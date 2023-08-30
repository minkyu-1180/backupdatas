# 백준 1331. 나이트 투어
import sys
sys.stdin = open("나이트투어input.txt")

chess = {'A' : 0,
         'B' : 1,
         'C' : 2,
         'D' : 3,
         'E' : 4,
         'F' : 5}

def change(string):
    i, j = chess[string[0]], int(string[1]) - 1
    return i, j

def go(i, j, ni, nj):
    if [ni-i, nj-j] in dir and [ni, nj] not in visited:
        visited.append([ni, nj])
        return True
    return False



# 나이트가 이동 가능한 방향
dir = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [2, -1], [1, -2], [2, 1], [1, 2]]

result = True
visited = []

arr = [input() for _ in range(36)]
i, j = change(arr[0])
visited.append([i, j])

y, x = change(arr[-1])

if go(i, j, y, x):
    idx = 1
    visited.pop() # 위에서 go로 인해 들어간end값 빼주기
    while idx < 36:
        ni, nj = change(arr[idx])
        if not go(i, j, ni, nj):
            result = False
            break
        i, j = ni, nj
        idx += 1

else:
    result = False


if result:
    print('Valid')
else:
    print('Invalid')