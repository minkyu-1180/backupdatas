# string
import sys
sys.stdin = open("Stringinput.txt", 'rt', encoding = 'UTF8')

for tc in range(1, 11):
    sc = int(input())
    pattern = input()
    target = input()

    N = len(target)
    M = len(pattern)
    i = 0
    j = 0
    c = 0

    while j < M and i < N:
        if target[i] != pattern[j]:
            i = i - j
            j = - 1
        i = i + 1
        j = j + 1

        if j == M:
            j = 0
            c += 1

    print(f'#{tc} {c}')