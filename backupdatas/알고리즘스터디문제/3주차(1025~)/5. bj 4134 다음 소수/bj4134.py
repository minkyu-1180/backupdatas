# 백준 4134. 다음 소수
import sys
sys.stdin = open("bj4134input.txt")

def isPrime(num):
    for i in range(2, int(num**(0.5)+1)):
        if num % i == 0:
            return False

    return True

T = int(input())
for tc in range(T):
    N = int(input())

    if N == 0 or N == 1 or N == 2:
        print(2)
    else:
        num = N
        while num <= 2*N:
            if isPrime(num):
                print(num)
                break
            num += 1
