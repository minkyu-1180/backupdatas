# IM 대비 23. GNS
import sys
sys.stdin = open("GNSinput.txt")
planet_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']


T = int(input())
for test_case in range(1, T+1):
    tc, N = map(str, input().split())
    arr = list(input().split())


    # 각 외계행성의 언어 개수를 순서대로 담기
    counts = [0] * 10
    for i, num in enumerate(planet_num):
        counts[i] = arr.count(num)

    print(f'#{test_case}')

    for i in range(10):
        num = counts[i]
        for _ in range(num):
            print(planet_num[i], end = ' ')
    print()


