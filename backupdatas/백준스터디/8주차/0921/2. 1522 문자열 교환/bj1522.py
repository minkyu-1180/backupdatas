# 백준 1522. 문자열 교환
import sys
sys.stdin = open("bj1522input.txt")


T = int(input())
for tc in range(T):
    string = input()
    result = int(1e9)
    a_c = string.count('a')
    s = len(string)
    # 시작점
    l = 0
    while l < s:
        # 오른쪽 끝값(+1)
        r = l+a_c
        # 범위 내에 존재
        if r <= s:
            new = string[l:r]
        # 넘어갈 경우
        else:
            new = string[l:s] + string[0:r-s]
        # a로 교환해야 하는 b의 개수
        if result > new.count('b'):
            result = new.count('b')
        l += 1
    print(result)
