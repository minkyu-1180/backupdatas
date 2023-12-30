# 백준 2661. 좋은 수열
import sys
sys.stdin = open("bj2661input.txt")


def backtracking(string):
    if len(string) == N:
        print(string)
        exit()

    for i in range(1, 4):
        flag = False
        new_string = string + str(i)
        for j in range(1, len(new_string) + 1):
            if new_string[-j:] == new_string[-2 * j:-j]:
                break
        else:
            flag = True
        if flag:
            backtracking(new_string)
    return
# N : 좋은 수열의 길이(1 <= N <= 80)
# 좋은 수열 중 가장 작은 수열 찾기
N = int(input())

# result = int(1e9)
backtracking('1')
# print(result)
