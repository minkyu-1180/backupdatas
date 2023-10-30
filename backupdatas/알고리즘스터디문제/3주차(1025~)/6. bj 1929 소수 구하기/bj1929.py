# 백준 1929. 소수 구하기
import sys
sys.stdin = open("bj1929input.txt")

def isPrime(num):
    for i in range(2, int(num**(0.5)+1)):
        if num % i == 0:
            return False

    return True
# 1 <= M <= N <= 1000000
# M 이상 N 이하의 소수 출력
M, N = map(int, input().split())

if M == 1:
    M = 2
for num in range(M, N+1):
    if isPrime(num):
        print(num)