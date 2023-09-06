# 백준 8979. 올림픽
import sys
sys.stdin = open("bj8979input.txt")
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())

    arr = []
    k_result = []
    for i in range(N):
        idx, gold, silver, bronze = map(int, input().split())
        if idx == K:
            k_result = [gold, silver, bronze]
        else:
            arr.append([gold,silver,bronze])


    counts = 1
    for other_result in arr:
        if k_result[0] < other_result[0]:
            counts += 1
        elif k_result[0] == other_result[0]:
            if k_result[1] < other_result[1]:
                counts += 1
            elif k_result[1] == other_result[1]:
                if k_result[2] < other_result[2]:
                    counts += 1
    print(counts)


