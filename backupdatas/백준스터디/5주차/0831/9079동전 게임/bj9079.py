# 백준 9079. 동전 게임
import sys
from collections import deque
sys.stdin = open("9079input.txt")

def solution(my_bit):
    cases = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    visited = [0] * 512

    now = 0
    for i in range(9):
        now += my_bit[i] * (2**i)

    if now == 0 or now == 511:
        return 0

    visited[now] = 1
    que = [my_bit]
    c = 1
    while que:
        now_bit = que.pop(0)
        for case in cases:
            flip(now_bit, case)

            cnt = 0
            for i in range(9):
                cnt += now_bit[i] * (2 ** i)
            if cnt == 0 or cnt == 511:
                return c
            if visited[cnt] == 0:
                visited[cnt] = c + 1
                que.append(now_bit)

            flip(now_bit, case)
        c += 1

    if 0 in visited:
        return -1


coin = {0:1,
        1:0}
def flip(bit, case):
    for c in case:
        bit[c] = coin[bit[c]]


    '''
    visited = [False] * 512
    visited[int(''.join(arr), 2)] = True
    # BFS
    queue = deque([(int(''.join(arr), 2), 0)])
    while queue:
        arrBin, count = queue.popleft()

        if arrBin == 0 or arrBin == 511:
            return count

        for numbers in cases:
            newArr = flip(numbers, list(bin(arrBin)[2:].zfill(9)))
            vs = int(''.join(newArr), 2)
            if not visited[vs]:
                visited[vs] = True
                queue.append((int(''.join(newArr), 2), count + 1))

    return -1
    '''




T = int(input())
for _ in range(T):
    arr = [list(input().split()) for _ in range(3)]

    my_bit = []
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 'H':
                my_bit.append(1)
            else:
                my_bit.append(0)
    print(my_bit)
    print(solution(my_bit))
