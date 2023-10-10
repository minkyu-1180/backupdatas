T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    shark_pos = (0, 0)
    fishes = []
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(N):
            if lst[j] == 9:
                shark_pos = (i, j)
                lst[j] = 0
            elif lst[j]:
                fishes.append((i, j, lst[j]))
        arr.append(lst)
    # print(arr)
    result = 0
    shark_size = 2
    c = 0
    while fishes:
        y, x = shark_pos
        min_dist = int(1e9)
        min_idx = -1
        for k in range(len(fishes)):
            i, j, fish_size = fishes[k]
            if shark_size < fish_size:
                continue
            dist = abs(i-y) + abs(j-x)
            if min_dist > dist:
                min_dist = dist
                min_idx = k
        if min_idx == -1:
            break

        ny, nx, size = fishes[min_idx]
        del fishes[min_idx]
        shark_pos = (ny, nx)
        result += min_dist
        if shark_size > size:
            c += 1
            if c == shark_size:
                shark_size += 1
                c = 0
    print(result)