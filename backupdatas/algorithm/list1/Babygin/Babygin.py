# 연습문제 2. Baby gin
import sys
sys.stdin = open("babygininput.txt")
T = int(input())

for test_case in range(1, T + 1):
    my_int = input().strip()

    counts = [0] * 10
    for i in my_int:
        counts[int(i)] += 1

    tri = 0
    run = 0
    # triplet 검사
    for i in range(10): # 0 ~ 9
        if counts[i] >= 3:
            p = counts[i] // 3
            counts[i] -= (p * 3)
            tri += p
    # run 검사
    for i in range(8): # 0 ~ 7
        l = counts[i]
        if l == counts[i+1] and l == counts[i+2]:
            if l != 0:
                counts[i] -= l
                counts[i+1] -= l
                counts[i+2] -= l
            run += l
    result = (run + tri)//2

    print(f'#{test_case} {result}')
