import sys
sys.stdin = open("bj2174input.txt")

A, B = map(int, input().split())
N, M = map(int, input().split())

arr = [[0] * (A+1) for _ in range(B+1)]
robot_position = [[] for _ in range(N+1)]

moving_F = {'N' : [1, 0],
          'W' : [0, -1],
          'S' : [-1, 0],
          'E' : [0, 1],
          }
moving_LR = {
             'N' : 0,
             'W' : 1,
             'S' : 2,
             'E' : 3,
             }

result = 'OK'

for i in range(1, N+1):
    x, y, d = map(str, input().split())
    x = int(x)
    y = int(y)
    arr[y][x] = i
    robot_position[i] = [y, x, d]

for _ in range(M):
    robot, cmd, cnt = map(str, input().split())
    robot = int(robot)
    cnt = int(cnt)
    i = robot_position[robot][0]
    j = robot_position[robot][1]
    position = robot_position[robot][2]

    if cmd == 'L':
        cnt %= 4
        robot_position[robot][2] = moving_LR[moving_LR[position] + cnt]

    elif cmd == 'R':
        cnt %= 4
        robot_position[robot][2] = moving_LR[moving_LR[position] - cnt]

    elif cmd == 'F':
        for k in range(cnt):
            di, dj = moving_F[position]
            ni = i + di
            nj = j + dj
            if 1 > ni or ni > B or 1 > nj or nj > A:
                if result == 'OK':
                    result = f'Robot {robot} crashes into the wall'
                break
            if arr[ni][nj]:
                if result == 'OK':
                    result = f'Robot{robot} crashes into robot{arr[ni][nj]}'
                break
            i = ni
            j = nj
        else:
            robot_position[robot][0] = i
            robot_position[robot][1] = j
            arr[i][j] = robot
            arr[robot_position[robot][0]][robot_position[robot][1]] = 0

print(result)