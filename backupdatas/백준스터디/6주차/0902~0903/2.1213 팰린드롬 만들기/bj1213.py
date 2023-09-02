# 백준 1213. 팰린드롬 만들기
import sys
sys.stdin = open("bj1213input.txt")

T = int(input())
for tc in range(T):

    string = list(input())
    odd_alpha = []
    string.sort()
    types_alpha = dict()
    for alpha in string:
        types_alpha[alpha] = string.count(alpha)
        if string.count(alpha)%2 and alpha not in odd_alpha:
            odd_alpha.append(alpha)

    if len(odd_alpha) > 1:
        print("I'm Sorry Hansoo")
    else:
        result1 = ''
        result2 = ''
        for alpha, num in types_alpha.items():
            result1 += alpha * (num//2)
            result2 = alpha * (num//2) + result2

        if len(odd_alpha) == 1:
            result1 += odd_alpha[0]
        result = result1 + result2
        print(result)


