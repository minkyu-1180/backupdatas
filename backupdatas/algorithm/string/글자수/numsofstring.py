# 글자수
import sys
sys.stdin = open("numsofstringinput.txt")
T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    # 가장 많은 글자의 개수
    max_v = 0

    for s1 in str1:
        # str1에 포함된 문자가 str1에 몇 개 있는지
        c = 0
        for s2 in str2:
            if s1 == s2:
                c += 1
        if max_v < c:
            max_v = c
    print(f'#{test_case} {max_v}')