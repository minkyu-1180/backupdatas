# 백준 7785. 회사에 있는 사람
import sys
sys.stdin = open("bj7785input.txt")

# N : 로그에 기록된 출립 기록의 수(2 <= N <= 10**6)
N = int(input())

result = set()
for _ in range(N):
    name, check = map(str, input().split())
    if check == 'enter':
        result.add(name)
    else:
        result.remove(name)

result = list(result)
for name in sorted(result, reverse=True):
    print(name)
