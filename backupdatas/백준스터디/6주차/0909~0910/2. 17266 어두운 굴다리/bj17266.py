# 백준 17266. 어두운 굴다리
import sys
sys.stdin = open("bj17266input.txt")

# 시작 가로등의 위치가 굴다리의 시작점으로부터 가로등의 높이보다 덜 멀리 있는지 확인
def start(s):
    if s <= h:
        return True
    return False

# 끝 가로등의 위치가 굴다리의 끝으로부터 가로등의 높이보다 덜 멀리 있는지 확인
def end(e):
    if e <= h:
        return True
    return False

def middle():
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] > 2 * h:
            return False
    return True

T = int(input())
for tc in range(T):
    N = int(input()) # 굴다리 길이(0 <= N <= 100000)
    M = int(input()) # 가로등 개수(0 <= M <= N)
    arr = list(map(int, input().split())) # 설치할 가로등의 위치 좌표(0 <= x <= N) - 오름차순, 중복 X

    h = 1
    while True:
        # 양 끝 가로등과 굴다리 시작/끝 사이 거리
        s = arr[0]
        e = N - arr[-1]
        # 처음으로 굴다리가 빛으로 가득 찰 경우
        if start(s) and end(e) and middle():
            break
        h += 1
    print(h)


