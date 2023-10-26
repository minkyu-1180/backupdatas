# 백준 2011. 암호코드
import sys
sys.stdin = open("bj2011input.txt")

def backtracking(idx, flag):
    global result

    s1 = int(string[idx])





# 원래 T는 없음
T = int(input())
for tc in range(T):
    # string : 5000자리 이하의 암호
    string = input()
    N = len(string)
    '''
    경우의 수
    가장 첫 글자까지 : 무조건 한 가지
    두번째 글자 : 앞글자와 연계해서
    세번째 글자 ~ 끝 글자 : 일단 0이 아니면 앞글자까지 쌓인 dp값 받고
    추가로, 앞글자랑 묶어서 decoding 가능 -> 그 앞글자까지 쌓인 dp값 받고
    '''
    if string[0] == '0':
        print(0)
    elif N == 1:
        print(1)
    else:
        dp = [0] * N
        dp[0] = 1
        for i in range(1, N):
            num1 = int(string[i])
            num2 = int(string[i-1]) * 10 + int(string[i])
            if i == 1:
                if num1 > 0:
                    dp[i] += 1
                if 10 <= num2 <= 26:
                    dp[i] += 1
            else:
                if num1 > 0:
                    dp[i] += dp[i-1]
                if 10 <= num2 <= 26:
                    dp[i] += dp[i-2]

        print((dp[N-1])%1000000)

