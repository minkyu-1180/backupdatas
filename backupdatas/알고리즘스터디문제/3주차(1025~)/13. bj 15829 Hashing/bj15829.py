# 백준 15829. Hashing
import sys
sys.stdin = open("bj15829input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # 문자열의 길이
    L = int(input())
    string = input() # 길이가 L인 문자열(only 소문자)

    r = 31
    M = 1234567891
    result = 0
    # r : 31, M : 1234567891
    for i in range(L):
        s = string[i]
        result += ((ord(s)-96) * (r**i))%M
    # 마지막에 더해지면서 기존 result값이 M보다 크거나 같아질 수 있음 -> 마지막에도 나머지
    print(result%M)
