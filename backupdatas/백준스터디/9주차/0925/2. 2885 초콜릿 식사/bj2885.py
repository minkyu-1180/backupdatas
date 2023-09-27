# 백준 2885. 초콜릿 식사
import sys
sys.stdin = open("bj2885input.txt")

K = int(input())
choco = 1
count = 0
while choco < K:
    choco *= 2
result1 = choco

if result1 == K:
    result2 = 0
else:
    size = 0
    while choco > 1:
        choco //= 2
        count += 1
        if size + choco == K:
            size += choco
            break
        if size + choco < K:
            size += choco
        if size + choco > K:
            continue
    result2 = count
print(result1, result2)