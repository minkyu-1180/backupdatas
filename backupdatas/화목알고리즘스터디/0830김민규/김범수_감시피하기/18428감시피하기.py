import sys
input = sys.stdin.readline

# 설치한 장애물 개수가 3개일 때 적절히 설치했는지 확인해주는 함수
# 백트래킹 사용
def obstacle(c): # c : 설치한 장애물 개수
    global result

    # 장애물 세 개 설치 완료
    if c == 3:
        # 설치 완료된 상황에서 bfs 실행 결과, 감시 실패(목표 달성)의 경우 -> 케이스를 찾음
        if bfs():
            result = True # 성공했다면 result를 true로 초기화
            return
    # 아직 세 개 설치 미완
    else:
        # 빈 공간 중 세 곳에 장애물 설치 진행(조합, Combination)
        for x in range(N):
            for y in range(N):
                if arr[x][y] == "X":
                    arr[x][y] = "O"
                    obstacle(c + 1) # backTracking
                    arr[x][y] = "X"

# 세 개의 장애물 설치 완료 후 감시여부 확인
def bfs():
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i, j in t_position:# 선생님의 위치에서
        for di, dj in dir: # 상/하/좌/우 탐색
            ni = i + di
            nj = j + dj
            while 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == "O": # 선생님 기준 학생보다 먼저 장애물 만남 -> 방향전환
                    break

                elif arr[ni][nj] == "S": # 선생님 기준 장애물보다 먼저 학생 만남 -> 해당 장애물 좌표에 대해 목표달성 실패
                    return False
                # X를 만난 경우 -> 같은 방향에 대해 탐색 진행
                ni += di
                nj += dj

    # no return -> 목표 달성 성공(해당 좌표에 장애물 설치시 감시 실패)
    return True


N = int(input())
result = False
arr = [list(input().split()) for _ in range(N)]
t_position = []

# 반복문을 통해 복도 정보를 입력 받는다.
for i in range(N):
    for j in range(N):
        if arr[i][j] == "T": # 선생님이 있는 좌표를 저장
            t_position.append([i, j])


# 설치한 장애물 개수 0으로 백트래킹 시작
obstacle(0)

# result == True 즉, 감시 실패 상황 있음
if result:
    print('YES')
# result == False 즉, 감시 실패 상황 없음(항상 감시)
else:
    print('NO')