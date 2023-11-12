# 백준 25192. 인사성 밝은 곰곰이
import sys
sys.stdin = open("bj25192input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 채팅창의 기록 수(1 <= N <= 100000)
    N = int(input())
    flag = False
    result = 0
    my_set = set()
    for _ in range(N):
        string = input()
        if string == 'ENTER':
            my_set = set()
        elif string not in my_set:
            my_set.add(string)
            result += 1
    print(result)