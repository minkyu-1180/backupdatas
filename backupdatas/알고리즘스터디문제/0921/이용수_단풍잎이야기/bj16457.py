# 백준 16457. 단풍잎 이야기
from itertools import combinations
import sys
sys.stdin = open("bj16457input.txt")

N, M, K = map(int, input().split())

stages = []
skills = set()
for _ in range(M):
    stage = list(map(int, input().split()))
    for s in stage:
        skills.add(s)
    stages.append(stage)

n_skills = list(combinations(skills, 3))
result = 0
for skills in n_skills:
    c = 0
    for stage in stages:
        for k in stage:
            if k not in skills:
                break
        else:
            c += 1
    if result < c:
        result = c
print(result)




