# 백준 1713. 후보 추천하기
from collections import deque
import sys
sys.stdin = open("후보추천input.txt")


N = int(input()) # 후보 수
M = int(input()) # 투표자 수

arr = list(map(int, input().split()))


que1 = deque([])
que2 = deque([])


while arr:
    std = arr.pop(0)
    if len(que1) < 3:
        que1.append(std)
        que2.append(1)
    elif len(que1) == 3:
        if std in que1: # 이미 등록된 경우
            que2[(que1.index(std))] += 1
        else:
            min_vote = min(que2)
            for i in range(3):
                if que2[i] == min_vote:
                    que1[i] = std
                    que2[i] =
                    que1.append(std)
                    que2.append(1)
                    break

print(*sorted(que1))


