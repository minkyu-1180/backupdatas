# 백준 19949. 영재의 시험
import sys
sys.stdin = open("bj19949input.txt")

def backtracking(idx, c):
    global result

    if c + (10 - idx) < 5:
        return

    if idx == 10:
        if c >= 5:
            result += 1
        return

    for i in range(1, 6):
        if idx >= 2 and yeongjae[idx-1] == i and yeongjae[idx-2] == i:
            continue
        yeongjae[idx] = i
        if arr[idx] == i:
            backtracking(idx+1, c+1)
        else:
            backtracking(idx+1, c)
        yeongjae[idx] = 1

arr = list(map(int, input().split()))
yeongjae = [0] * 10
result = 0
backtracking(0, 0)
print(result)