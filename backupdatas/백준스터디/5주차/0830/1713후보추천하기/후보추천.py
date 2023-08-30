# 백준 1713. 후보 추천하기
from collections import deque
import sys
sys.stdin = open("후보추천input.txt")


N = int(input()) # 후보 수
M = int(input()) # 투표자 수

arr = list(map(int, input().split()))

que1 = []
que2 = []

for std in arr:
    if std in que1:
        que2[que1.index(std)] += 1
    else:
        if len(que1) == N:
            min_v = min(que2)
            for i in range(len(que1)):
                if que2[i] == min_v:
                    que1.pop(i)
                    que2.pop(i)
                    break
            que1.append(std)
            que2.append(1)

        else:
            que1.append(std)
            que2.append(1)

que1.sort()
print(*que1)
