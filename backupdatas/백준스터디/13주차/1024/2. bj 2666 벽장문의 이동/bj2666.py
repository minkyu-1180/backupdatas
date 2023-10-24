# 백준 2666. 벽장문의 이동
import sys
sys.stdin = open("bj2666input.txt")

# a, b : 현재 열려있는 위치
# i : 열어서 사용하려는 arr에 저장된 문의 인덱스값
# 지금까지 쌓여온 옮긴 횟수
def backtracking(a, b, i, c):
    global result

    # result가 갱신 된 적이 있으면서, 이미 현재 상태에서 result보다 커진 경우 -> 종료
    if result != int(1e9) and c >= result:
        return
    # 끝까지 도달한 경우(모든 열려고 하는 문에 대한 처리) -> result 갱신
    if i == M:
        if result > c:
            result = c
        return
    # 현재 열려고 하는 문의 번호
    door = arr[i]
    # 이미 열려있는 문일 경우 -> 열려있는 문 번호 그대로, idx만 증가(횟수도 변화 X)
    if door == a or door == b:
        backtracking(a, b, i+1, c)
    # 닫혀있는 문을 열려고 한 경우
    else:
        # a보다 왼쪽에 있는 문 열려고 하면 -> 무조건 door의 닫힌 문부터 a로 밀어넣는게 이득
        if door < a:
            backtracking(door, b, i+1, c+(a-door))
        # a와 b 사이에 있는 문 열려고 하면
        # 거리와 상관없이 둘 다 해봄
        # 지금 더 가까이 열려있는 문쪽으로 미는게 당장은 좋아보여도, 나중에 더 별로일수도
        elif a < door < b:
            backtracking(door, b, i+1, c+(door-a))
            backtracking(a, door, i+1, c+(b-door))
        # b보다 오른쪽에 있는 문 열력 ㅗ하면 -> 무조건 door의 닫힌 문부터 b로 밀어넣는게 이득
        elif b < door:
            backtracking(a, door, i+1, c+(door-b))

# N : 벽장의 개수(3 <= N <= 20)
N = int(input())
# 초기에 열려있는 두 개의 벽장 번호
s1, s2 = map(int, input().split())
# 그냥 idx로 번호 알고 싶어서 -1
s1 -= 1
s2 -= 1
# M : 사용할 벽장들의 개수(M <= 20)
M = int(input())
# 사용할 벽장 번호를 담을 배열
arr = []
for _ in range(M):
    # 여기도 idx로 접근할거라 -1
    arr.append(int(input())-1)
# print(arr)
result = int(1e9)

# a, b가 크기순으로 들어가고 싶어서 min, max로 넣기
backtracking(min(s1, s2), max(s1, s2), 0, 0)
print(result)