# sw academy 토너먼트 카드게임
import sys
sys.stdin = open("cardgameinput.txt")


def win(idx1, idx2):
    if arr[idx1] == arr[idx2] or arr[idx1] % 3 == (arr[idx2] + 1) % 3:
        return idx1
    else:
        return idx2
def func(start, end):
    # 부전승
    if end == start:
        return start

    middle = (start + end) // 2
    idx1 = func(start, middle)
    idx2 = func(middle+1, end)
    return win(idx1, idx2)



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{test_case} {func(0, N-1) + 1}')
