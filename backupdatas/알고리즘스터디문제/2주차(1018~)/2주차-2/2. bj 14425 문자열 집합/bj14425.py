# 백준 14425. 문자열 집합
import sys
sys.stdin = open("bj14425input.txt")

# N : 집합 S의 문자열 개수(1<= N <= 10000)
# M : 입력으로 주어지는 문자열 개수(1 <= M <= 10000)
N, M = map(int, input().split())
# S : N개의 문자열을 포함하고 있는 집합
S = set()
for _ in range(N):
    S.add(input())

# M개의 문자열 중, S에 포함된 문자열 개수
result = 0
for _ in range(M):
    string = input()
    result += int(string in S)
print(result)
