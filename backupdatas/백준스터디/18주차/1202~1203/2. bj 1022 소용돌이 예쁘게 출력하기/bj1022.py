# 백준 1022. 소용돌이 예쁘게 출력하기
import sys
sys.stdin = open("bj1022input.txt")

'''
     -3  -2  -1  0  1  2  3
    -----------------------
-3 | 37  36  35 34 33 32 31
-2 | 38  17  16 15 14 13 30
-1 | 39  18   5  4  3 12 29
 0 | 40  19   6  1  2 11 28
 1 | 41  20   7  8  9 10 27
 2 | 42  21  22 23 24 25 26
 3 | 43  44  45 46 47 48 49 

- 1 : (0, 0)
- 2 ~ 9 : (-1, -1) ~ (1, 1)
- 10 ~ 25 : (-2, -2) ~ (2, 2)
'''

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # (r1, c1) : 가장 왼쪽 위
    # (r2, c2) : 가장 오른쪽 위
    # r1과 r2, c1과 c2는 같을수도
    r1, c1, r2, c2 = map(int, input().split())

    # 총 돌려야 할 횟수
    total_c = (r2-r1+1) * (c2-c1+1)
    # 채울 소용돌이 모양
    arr = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
    # 모양 맞추기 위해 띄울 칸 정하기
    max_n = 0

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            val = 0
            # 둘 중 더 큰 값 정해서 테두리 선택
            max_val = max(abs(i), abs(j))
            # 더 큰 값의 가장 오른쪽 아래 설정
            # ex. i : -1, j : 2 -> max_val = 2 / length : 3 ** 2 + 1 : 10
            end_val = (max_val * 2 - 1) ** 2 + 1

            # 둘중 큰 값이 abs(i)일 경우
            if max_val == abs(i):
                # 음이 아닌 정수
                if max_val == i:
                   val = end_val + max_val * 7 + j - 1
                # 음의 정수
                else:
                    val = end_val + max_val * 3 - j - 1
            # 둘중 큰 값이 abs(j)일 경우
            else:
                if max_val == j:
                    val = end_val + max_val * 1 - i - 1
                else:
                    val = end_val + max_val * 5 + i - 1
            # 채울 값 찾기
            ni = i - r1
            nj = j - c1

            arr[ni][nj] = val
            # 가장 큰 값 초기화
            if max_n < val:
                max_n = val

    # 가장 큰 값의 길이로 바꾸기
    max_len = len(str(max_n))
    # 다 채운 후 출력
    for i in range(r2-r1+1):
        for j in range(c2-c1+1):
            val = str(arr[i][j])
            plus = ' ' * (max_len - len(val))
            print(plus + val, end=' ')
        print()
