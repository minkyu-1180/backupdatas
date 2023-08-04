# sw academy - 18075. Gravity
import sys
sys.stdin = open("gravityinput.txt")

T = int(input())

for test_case in range(1, T + 1):
    # 방의 가로 길이
    N = int(input())

    arr = list(map(int, input().split()))
    # arr의 i번 인덱스 뒤쪽에 본인보다 크거나 같은 값이 몇개인지 세어서 반환해주는 리스트
    over_list = [0] * N

    for i in range(len(arr)):
        over_count = 0

        for j in range(i+1, len(arr)):
            if arr[i] <= arr[j]:
                over_count += 1
        over_list[i] = over_count
    result_list = [0] * N
    max = 0
    for i in range(N):
        result = (N-i-1) - over_list[i]
        if result > max:
            max = result
    print(f'#{test_case} {max}')





'''
52 : 0번 index & 자기보다 큰 값이 몇개?
.
.
.
.


'''