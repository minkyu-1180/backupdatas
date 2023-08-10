# 2941. 크로아티아 알파벳
import sys
sys.stdin = open("2941input.txt")

cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

T = int(input())
for test_case in range(1, T+1):
    target = input()

    for pattern in cro_alpha:
        target = target.replace(pattern, '!')
    print(len(target))
