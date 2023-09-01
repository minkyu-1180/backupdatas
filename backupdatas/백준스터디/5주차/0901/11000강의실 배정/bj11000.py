# 백준 11000. 강의실 배정
import sys
sys.stdin = open("11000input.txt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x : x[1])

class_lst = []
class_lst.append([0])

for i in range(1, N):
    n_s, n_e = arr[i][0], arr[i][1]
    for cls in class_lst:
        idx = cls[-1]
        s, e = arr[idx]
        if e <= n_s:
            cls.append(i)
            break
    else:
        class_lst.append([i])

print(len(class_lst))