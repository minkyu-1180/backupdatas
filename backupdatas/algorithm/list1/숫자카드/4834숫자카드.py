# sw academy - 4834. 숫자카드
import sys
sys.stdin = open("숫자카드input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    n_string = input()

    counts = [0] * 10
    for i in n_string:
        counts[int(i)] += 1

    result = [0] * 2

    for i in range(10):
        if counts[i] >= result[1]:
            result[0] = i
            result[1] = counts[i]




    print(f'#{test_case} {result[0]} {result[1]}')


