# sw academy 피자굽기
import sys
sys.stdin = open("피자굽기input.txt")

T = int(input())
for test_case in range(1, T+1):
    # N : 피자 화덕 크기(화덕 내에 들어갈 수 있는 피자의 수)
    # M : 피자 개수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    new_arr = [[0, 0] for _ in range(M)]

    # new_arr의 각 idx : [v, i]
    # v : 해당 피자의 치즈량 / i : 해당 피자 번호
    for i, v in enumerate(arr):
        new_arr[i][0] = v
        new_arr[i][1] = i+1
    # 치즈가 다 녹아서 완성된 피자의 번호 순서
    result = []

    # 가장 최근 화덕에 넣은 피자의 idx
    last = N-1

    # 처음에 아예 넣어주고 시작(enqueue를 N번 시행한 상태)
    queue = []
    for i in range(N):
        queue.append(new_arr[i])
    front = 0

    while len(result) < M:
        queue[front][0] //= 2
        if queue[front][1] > 0 and queue[front][0] == 0:
            result.append(queue[front][1])
            if last + 1 < M:
                queue[front] = new_arr[last + 1]
                last += 1
            else:
                # queue의 size는 불변
                # 거의 모든 피자의 치즈가 녹았을 때, 화덕 내에 빈 칸 발생
                # 해당 빈칸을 채워주지만, 위의 조건문에서는 걸리지 않는 ele 생성
                queue[front] = [0, -1]
        # front 증가
        front = (front + 1) % N
    print(f'#{test_case} {result[-1]}')


