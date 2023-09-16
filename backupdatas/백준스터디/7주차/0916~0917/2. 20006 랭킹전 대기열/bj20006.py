# 백준 20006. 랭킹전 대기열
import sys
sys.stdin = open("bj20006input.txt")
p, m = map(int, input().split()) # p : 플레이어 수 / m : 방의 정원

rooms = []

for _ in range(p):
    level, nickname = input().split()
    level = int(level)
    player_info = [level, nickname]
    # 방 존재 X -> 새로운 방 만들기
    if not rooms:
        room = [player_info]
        rooms.append(room)
    else:
        for room in rooms:
            if len(room) < m and abs(level - room[0][0]) <= 10:
                room.append(player_info)
                break
        else:
            room = [player_info]
            rooms.append(room)

for room in rooms:
    room.sort(key=lambda x: x[1])
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')

    for level, nick in room:
        print(level, nick)

