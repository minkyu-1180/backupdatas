# 백준 1244. 스위치 켜고 끄기
import sys
sys.stdin = open("1244input.txt")
N = int(input())

# 스위치 상태
# i번 idx : i번 스위치 상태(1 : 켜짐 / 0 : 꺼짐)
arr = [0] + list(map(int, input().split()))

switch = {0:1,
          1:0}
M = int(input()) # 학생 수
for i in range(M):
    # sex : 성별(남 : 1 / 여 : 2)
    # idx : 관련된 스위치 번호
    sex, idx = map(int, input().split())
    # 남자 : 스위치의 배수들 변화
    if sex == 1:
        for s in range(1, N+1):
            if s%idx == 0:
                arr[s] = switch[arr[s]]
    # 여자 : 스위치 기준 좌우대칭 최대만큼 변화화    elif sex == 2:
    elif sex == 2:
        arr[idx] = switch[arr[idx]]
        l = 1
        while True:
            if 1 <= idx-l and idx+l <= N and arr[idx-l] == arr[idx+l]:
                arr[idx-l] = arr[idx+l] = switch[arr[idx+l]]
                l += 1
            else:
                break

for i in range(1, N+1):
    print(arr[i], end = ' ')
    if i % 20 == 0:
        print()