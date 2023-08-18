# 종이 붙이기
import sys
sys.stdin = open("paperinput.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    end = N // 10
    memo = [0] * 31
    memo[0] = 1
    memo[1] = 1
    for i in range(2, 31):

        memo[i] = memo[i-1] + 2 * memo[i-2]
    print(f'#{test_case} {memo[N//10]}')




