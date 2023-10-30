# 백준 18110. solved.ac
import sys
sys.stdin = open("bj18110input.txt")

def function(a, b):
    # print(a/b)
    if (a/b - a//b) < 0.5:
        return a//b
    else:
        return a//b + 1

# 원래 T는 없음
T = int(input())
for tc in range(T):
# N : 난이도 의견의 개수(0 <= N <= 3x10**5)
N = int(input())
if N == 0:
    print(0)
else:
    num = function(N*15, 100)
    # print(num)
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()

    sum_score = sum(arr)
    # print(sum_score)
    for i in range(num):
        sum_score -= arr[i]
        sum_score -= arr[N-1-i]
    # print(sum_score)
    # print(arr)
    # for i in range(num, N-num):
    #     sum_score += arr[i]
    #
    result = function(sum_score, N-2*num)
    print(result)
