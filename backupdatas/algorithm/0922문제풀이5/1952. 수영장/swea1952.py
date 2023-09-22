# swea 1952. 수영장
import sys
sys.stdin = open("swea1952input.txt")

def backtracking(c, sum_cost):
    global result

    # 가지치기
    if result <= sum_cost:
        return

    if c >= 12:
        result = min(result, sum_cost)
        return

    if arr[c]:
        backtracking(c+1, sum_cost + (arr[c] * day))
        backtracking(c+1, sum_cost + month)
        backtracking(c+3, sum_cost + three_month)
        backtracking(c+12, sum_cost + year)
    else:
        backtracking(c+1, sum_cost)

T = int(input())
for tc in range(1, T+1):
    day, month, three_month, year = map(int, input().split())
    arr = list(map(int, input().split()))
    result = int(1e9)
    backtracking(0, 0)
    print(f'#{tc} {result}')

