# 백준 10989. 수 정렬하기 3
import sys
sys.stdin = open("bj10989input.txt")

# 수의 개수(1<=N<=10000000)
# 주어지는 수 : <=10000
N = int(input())
counts = [0] * (10001)
for _ in range(N):
    counts[int(input())] += 1

c = 0 # 현재 출력한 수
i = 1 # 현재 봐야하는 시작 수(~ i-1번 idx까지는 이미 다 출력)
while c < N:
    for j in range(i, 10001):
        # input에 j가 있었을 경우
        if counts[j]:
            # 입력된 j의 개수
            num = counts[j]
            for _ in range(num):
                print(j)
                c += 1
            i = j+1
            break

