# 백준 10473. 인간 대포
import sys
sys.stdin = open("bj10473input.txt")
import heapq


# 다른 노드로 걸어갈때 걸리는 시간
def walk(node1, node2):
    return (((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2)**0.5) / 5 # 초속 5m/s


# 다른 노드로 대포를 타고 갈때 걸리는 시간
def cannon(node1, node2):
    return (abs(((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2)**0.5 - 50) / 5) + 2 # 2초동안 탑승 -> 50m 날아가기

# 다익스트라
def dijkstra(start):
    pq = []
    # 우선순위 큐( 거리, 노드)를 사용하여 노드를 방문 순서대로 관리
    # 출발점 추가
    heapq.heappush(pq, (0, start))
    while pq:
        dist, now = heapq.heappop(pq)
        node1 = arr[now] # 현재 노드의 좌표 정보

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if times[now] < dist:
            continue

        # 모든 대포 확인
        for next in range(N + 2):
            node2 = arr[next] # 다음 노드의 좌표 정보
            # 걸어갔을 경우 시간
            time = walk(node1, node2)
            # 대포 포함 -> 날아가기 가능 -> 갱신해보기
            if now != 0 and now != (N + 1):
                time = min(time, cannon(node1, node2))

            # 이미 쌓여있는 시간이 현재 누적 시간보다 클 경우 -> 갱신 가능
            if times[next] > dist + time:
                # 갱신 후 힙큐에 삽입
                times[next] = dist + time
                heapq.heappush(pq, (dist + time, next))

# 노드에 순서대로 N + 2 개의 점을 넣어준다.(출발점 + N개 대포 + 도착점)
arr = []
start = list(map(float, input().split()))
end = list(map(float, input().split()))

# 시작점과 ~ 도착점 순으로 각 노드별 좌표 정보 넣어주기
arr.append(start)
N = int(input())
for _ in range(N):
    arr.append(list(map(float, input().split())))
arr.append(end)

# print(arr)
# times[i] : 시작점(0번 idx)에서 i로 가는데 걸리는 최소 시간
times = [int(1e9)] * (N + 2)

dijkstra(0)
# print(times)
print(round(times[N+1], 6))