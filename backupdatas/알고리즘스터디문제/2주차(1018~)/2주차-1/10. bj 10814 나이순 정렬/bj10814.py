# 백준 10814. 나이순 정렬
import sys
sys.stdin = open("bj10814input.txt")
# N : 온라인 저지 회원 수(1<=N<=100000)
N = int(input())

# ages[i] : 나이가 i살인 사람들의 이름(들어온 순으로 idx 부여)
ages = [[] for _ in range(201)]
for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)

    ages[age].append(name)
for i in range(1, 201):
    if ages[i]:
        names = ages[i]
        for name in names:
            print(i, name)