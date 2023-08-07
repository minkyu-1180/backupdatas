# 1357. 뒤집힌 덧셈
import sys
sys.stdin = open("1357input.txt")
T = int(input())

def Rev(num):
    result = 0
    n1 = num % 10
    n2 = (num % 100 - num % 10) // 10
    n3 = (num % 1000 - num % 100) // 100
    n4 = num // 1000


    result = n1 * 1000 + n2 * 100 + n3 * 10 + n4
    i = 1
    while i <= 3:
        if result % (10 ** i) != 0:
            break
        i += 1
    result = result // (10 ** (i-1))
    return result




for test_case in range(1, T+1):
    X, Y = map(int, input().split())
    print(Rev(Rev(X) + Rev(Y)))

