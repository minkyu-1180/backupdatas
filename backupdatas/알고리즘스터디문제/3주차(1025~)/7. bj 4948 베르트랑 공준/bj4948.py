# 백준 4948. 베르트랑 공준
import sys
sys.stdin = open("bj4948input.txt")

def isPrime(num):
    for i in range(2, int(num**(0.5)+1)):
        if num % i == 0:
            return False

    return True
N = int(input())
while True:
    if N == 0:
        break

    result = 0
    for num in range(N+1, 2*N+1):
        if isPrime(num):
            result += 1
    print(result)



    N = int(input())