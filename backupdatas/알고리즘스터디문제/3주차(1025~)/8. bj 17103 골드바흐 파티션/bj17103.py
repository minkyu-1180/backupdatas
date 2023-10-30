# 백준 17103. 골드바흐 파티션
import sys
sys.stdin = open("bj17103input.txt")

def isPrime(num):
    for i in range(2, int(num**(0.5)+1)):
        if num % i == 0:
            return False

    return True

primes = []
arr = [0] * 1000001
arr[0] = arr[1] = 1
for i in range(2, 1000001):
    if arr[i] == 1:
        continue
    if arr[i] == 0:
        primes.append(i)
        for j in range(2*i, 1000001, i):
            arr[j] = 1

T = int(input())
for tc in range(T):
    N = int(input())

    result = 0
    for p in primes:
        if p >= N:
            break
        if p <= N-p and arr[N-p] == 0:
            result += 1
    print(result)