# 백준 5582. 공통 부분 문자열
import sys
sys.stdin = open("bj5582input.txt")
from pprint import pprint
# 원래 T는 없음
T = int(input())
for tc in range(T):
    string1 = input()
    string2 = input()
    if len(string1) >= len(string2):
        max_len_str = string1
        min_len_str = string2
    else:
        max_len_str = string2
        min_len_str = string1
    # dp[i][j] : 더 긴 길이의 문자열의 i번 idx까지, 더 짧은 문자열의 j번 idx까지 비교했을 때
    # max[i]가 min[j]랑 다른 경우는 0(~i, ~j까지 이어져온 동일 연속 문자열)
    # 같은 경우는, 그 전 값을 받음(만약, ~(i-1), ~(j-1)까지 봤을 때, 끊겨있을 경우, 1이되고, 이어져있을 경우 추가됨)
    dp = [[0] * len(min_len_str) for _ in range(len(max_len_str))]

    i = 0
    while i < len(max_len_str):
        # 처음으로 같아지는 순간 -> 그 뒤로는 다 같음
        if max_len_str[i] == min_len_str[0]:
            # print('i : ', i)
            break
        i += 1
    for k in range(i, len(max_len_str)):
        dp[k][0] = 1

    j = 0
    while j < len(min_len_str):
        # 처음으로 같아지는 순간 -> 그 뒤로는 다 1
        if min_len_str[j] == max_len_str[0]:
            # print('j : ', j)
            break
        j += 1
    for k in range(j, len(min_len_str)):
        dp[0][k] = 1
    # pprint(dp)

    result = 0
    for i in range(1, len(max_len_str)):
        for j in range(1, len(min_len_str)):
            # max_len_str의 i번 문자와 min_len_str의 j번 문자가 다름 -> dp 상태 변화 X
            if max_len_str[i] != min_len_str[j]:
                # 이어받기
                continue
            else:
                dp[i][j] = dp[i-1][j-1] + 1
                if result < dp[i][j]:
                    result = dp[i][j]

    # pprint(dp)
    # print()

    # print(dp[len(max_len_str)-1][len(min_len_str)-1])
    print(result)