# 백준 1963. 소수 경로
import sys
from collections import deque
sys.stdin = open("bj1963input.txt")

def is_prime(num):
    for n in range(2, int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def bfs():
    que = deque()
    visited = set()

    que.append((START, 0))
    visited.add(START)

    while que:
        now, cnt = que.popleft()
        if now == END:
            return cnt
        s1, s2, s3, s4 = list(now)

        # s1에 대해
        for i in range(1, 10):
            si = str(i)
            next = si+s2+s3+s4
            if is_prime(int(next)) and next not in visited:
                que.append((next, cnt+1))
                visited.add(next)

        for i in range(10):
            si = str(i)
            next1 = s1+si+s3+s4
            next2 = s1+s2+si+s4
            next3 = s1+s2+s3+si

            if is_prime(int(next1)) and next1 not in visited:
                que.append((next1, cnt+1))
                visited.add(next1)
            if is_prime(int(next2)) and next2 not in visited:
                que.append((next2, cnt+1))
                visited.add(next2)
            if is_prime(int(next3)) and next3 not in visited:
                que.append((next3, cnt+1))
                visited.add(next3)

    return 'Impossible'
T = int(input())
for tc in range(T):
    # START -> END로 바꾸는게 목표
    # 편하게 바꾸려고 str로
    START, END = map(str, input().split())
    print(bfs())
